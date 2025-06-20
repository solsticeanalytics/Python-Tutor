from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import json
import time
from datetime import datetime
import uuid

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active connections and their messages
active_connections = {}
connection_messages = {}

class Message(BaseModel):
    text: str
    connection_id: str | None = None

# 1. Long Polling endpoints
@app.post("/poll")
async def poll_endpoint(message: Message | None = None):
    # Generate unique connection ID if not exists
    connection_id = message.connection_id if message and message.connection_id else str(uuid.uuid4())
    
    # Initialize connection data structures if needed
    if connection_id not in active_connections:
        active_connections[connection_id] = {
            "last_seen": datetime.now(),
            "message_count": 0
        }
    if connection_id not in connection_messages:
        connection_messages[connection_id] = []
    
    # Update last seen time
    active_connections[connection_id]["last_seen"] = datetime.now()
    
    # If there's a message to send, queue it
    if message and message.text:
        msg = f"{message.text} (at {datetime.now().strftime('%H:%M:%S')})"
        connection_messages[connection_id].append(msg)
        active_connections[connection_id]["message_count"] += 1
        return {
            "message": msg,
            "connection_id": connection_id,
            "type": "message",
            "count": active_connections[connection_id]["message_count"]
        }
    
    # Check for queued messages first
    if connection_messages[connection_id]:
        msg = connection_messages[connection_id].pop(0)
        return {
            "message": msg,
            "connection_id": connection_id,
            "type": "queued_message",
            "count": active_connections[connection_id]["message_count"]
        }
    
    # If no messages, hold the connection
    try:
        for _ in range(30):  # Wait for max 30 seconds
            await asyncio.sleep(1)
            # Check for new messages that arrived while waiting
            if connection_messages[connection_id]:
                msg = connection_messages[connection_id].pop(0)
                return {
                    "message": msg,
                    "connection_id": connection_id,
                    "type": "new_message",
                    "count": active_connections[connection_id]["message_count"]
                }
        
        # No messages after timeout
        active_connections[connection_id]["message_count"] += 1
        return {
            "message": f"No new messages (timeout at {datetime.now().strftime('%H:%M:%S')})",
            "connection_id": connection_id,
            "type": "timeout",
            "count": active_connections[connection_id]["message_count"]
        }
    except:
        # Handle disconnection
        return {
            "message": "Connection error",
            "connection_id": connection_id,
            "type": "error",
            "count": active_connections[connection_id]["message_count"]
        }

# 2. Server-Sent Events endpoints
@app.post("/sse/message")
async def sse_message(message: Message):
    if message.connection_id in connection_messages:
        msg = f"{message.text} (at {datetime.now().strftime('%H:%M:%S')})"
        connection_messages[message.connection_id].append(msg)
        return {"status": "Message sent", "message": msg}
    return {"status": "Connection not found"}

@app.get("/sse")
async def sse_endpoint():
    connection_id = str(uuid.uuid4())
    connection_messages[connection_id] = []
    counter = 0
    
    async def event_generator():
        nonlocal counter
        while True:
            # Check for user messages
            if connection_messages[connection_id]:
                for msg in connection_messages[connection_id]:
                    yield f"data: {json.dumps({'message': msg, 'connection_id': connection_id})}\n\n"
                connection_messages[connection_id].clear()
            
            # Send heartbeat message
            counter += 1
            yield f"data: {json.dumps({'message': f'Message {counter}', 'connection_id': connection_id})}\n\n"
            await asyncio.sleep(1)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

# 3. WebSocket endpoints
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connection_id = str(uuid.uuid4())
    connection_messages[connection_id] = []
    counter = 0
    
    try:
        while True:
            # Check for incoming messages
            try:
                data = await asyncio.wait_for(websocket.receive_json(), timeout=0.1)
                if "message" in data:
                    msg = f"{data['message']} (at {datetime.now().strftime('%H:%M:%S')})"
                    connection_messages[connection_id].append(msg)
                    await websocket.send_json({
                        "message": msg,
                        "connection_id": connection_id,
                        "type": "user_message"
                    })
            except asyncio.TimeoutError:
                pass
            except:
                if len(connection_messages[connection_id]) > 0:
                    await websocket.send_json({
                        "message": connection_messages[connection_id][-1],
                        "connection_id": connection_id,
                        "type": "user_message"
                    })
                    connection_messages[connection_id].clear()
            
            # Send heartbeat message
            counter += 1
            await websocket.send_json({
                "message": f"Message {counter}",
                "connection_id": connection_id,
                "type": "heartbeat"
            })
            await asyncio.sleep(1)
    except:
        await websocket.close()
    finally:
        if connection_id in connection_messages:
            del connection_messages[connection_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
