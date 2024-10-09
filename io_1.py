import asyncio

async def task1():
    try:
        await asyncio.sleep(2)  # Simulate some I/O operation
    except Exception as e:
        print(f"Task 1 encountered an error: {e}")

async def task2():
    try:
        await asyncio.sleep(2)  # Simulate some I/O operation
    except Exception as e:
        print(f"Task 2 encountered an error: {e}")

async def run_tasks():
    try:
        await task1()
        await task2()
    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    asyncio.run(run_tasks())
