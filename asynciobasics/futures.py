import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    # set the result of the future
    future.set_result(value)
    print(f"set the future's result to: {value}")
    
async def main():
    # manually create event loop
    event_loop = asyncio.get_running_loop()
    # create future obj in that loop
    future = event_loop.create_future()
    
    # schedule the setting of the future's result
    asyncio.create_task(set_future_result(future, "the value I set on the future's value"))
    
    # await that future
    result = await future
    print(f"received the future's result: {result}")
    
asyncio.run(main())