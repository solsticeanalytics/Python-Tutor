# Data Transport Methods Demo

This project demonstrates three real-time data transport protocols using FastAPI (server) and JavaScript (client):

- **Long Polling**
- **Server-Sent Events (SSE)**
- **WebSocket**

Each method is fully implemented and can be tested from the included HTML client.

## Overview of Transport Methods

### 1. Long Polling

- Client sends a POST request to establish a connection and receives a unique connection ID.
- Server holds the connection open if no data is available, or responds immediately if there is data.
- Supports message queuing, timeouts, and connection state tracking.

### 2. Server-Sent Events (SSE)

- Client opens a persistent HTTP connection to receive a stream of events from the server.
- Messages are sent from server to client as they become available.
- Heartbeat messages are sent periodically to keep the connection alive.
- Client can send messages to the server via a POST endpoint.

### 3. WebSocket

- Client establishes a full-duplex WebSocket connection.
- Supports real-time, bidirectional communication.
- Heartbeat messages are sent from server to client.
- Each connection is isolated and messages are scoped per connection.

## How to Run

1. Start the server:

   ```bash
   python transport_server.py
   ```

2. Open the client:

   - Open `transport_client.html` in a web browser
   - Use the "Start" button in any of the three sections (Long Polling, SSE, WebSocket) to initiate a connection

## Testing the Features

For each transport method, you can:

1. **Basic Connection**
   - Click "Start" in the desired section
   - Observe the connection ID or initial message
   - For Long Polling and SSE, notice periodic heartbeat or timeout messages

2. **Message Sending**
   - Type a message in the input field
   - Click "Send"
   - Observe immediate message delivery in the message area

3. **Multiple Clients**
   - Open multiple browser tabs
   - Start connections in each tab (for any method)
   - Observe separate connection IDs/messages
   - Send messages from different tabs and verify isolation

4. **Connection Handling**
   - Close a browser tab
   - Observe server cleanup (where applicable)
   - Reopen and reconnect
   - Verify new connection establishment

5. **Message Queueing and Ordering**
   - Send multiple messages quickly
   - Observe ordered delivery and timestamps

## Protocol Flow

### Long Polling

```text
Client → Server: POST /poll
Server → Client: {connection_id: "uuid", type: "timeout"}

Client → Server: POST /poll {text: "message", connection_id: "uuid"}
Server → Client: {message: "text", type: "message"}

Client → Server: POST /poll {connection_id: "uuid"}
... server holds connection ...
Server → Client: {message: "data"} or timeout after 30s
```

### Server-Sent Events (SSE)

```text
Client → Server: GET /sse (opens event stream)
Server → Client: data: {message: "...", connection_id: "uuid"}

Client → Server: POST /sse/message {text: "message", connection_id: "uuid"}
Server → Client: (message is queued and sent on next event)
```

### WebSocket

```text
Client → Server: WebSocket /ws (opens connection)
Server → Client: {message: "Message N", connection_id: "uuid", type: "heartbeat"}

Client → Server: {message: "text"}
Server → Client: {message: "text", connection_id: "uuid", type: "user_message"}
```

## Implementation Details

### Server-Side Features

- Connection tracking and message queuing per connection
- Timeout and heartbeat handling with asyncio
- Error handling and connection cleanup
- Three separate endpoints for Long Polling, SSE, and WebSocket

### Client-Side Features

- Automatic reconnection (where applicable)
- Connection ID management
- Error handling and retry logic
- Message display with timestamps
- Clean connection termination
- Unified UI for all three transport methods

## Best Practices Demonstrated

1. **Reliability**
   - Unique connection IDs
   - Message queuing and delivery guarantees
   - Error handling and reconnection

2. **Performance**
   - Efficient connection holding and event streaming
   - Quick response for available data
   - Proper connection cleanup

3. **Security**
   - Connection isolation
   - Message scoping
   - Error state handling

4. **Monitoring**
   - Connection state tracking
   - Message counting
   - Timestamp logging

## Common Issues and Solutions

1. **Lost Connections**
   - Server detects timeouts and cleans up
   - Client can reconnect automatically
   - Messages are preserved in queue (where applicable)

2. **Message Ordering**
   - FIFO queue implementation
   - Timestamp tracking
   - Sequential delivery

3. **Resource Management**
   - Connection cleanup
   - Memory management
   - Timeout limitations
