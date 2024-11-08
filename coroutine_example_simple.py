import asyncio

async def sim_fetch_with_delay(delay: int):
    """Coroutine that simulates a IO operation with a delay
    via sleep. 
    Args:
        delay (int): seconds to wait
    """
    print(f"fetching data with a delay of {delay} seconds")
    await asyncio.sleep(delay) 
    print("data fetched")
    return {"data": "some data"}

async def main():
    """Coroutine that calls another coroutine."""
    print("start of main coroutine")
    coroutine_obj = sim_fetch_with_delay(2)
    
    # await the coroutine
    # pauses main until coroutine completes
    result = await coroutine_obj
    print(f"received result: {result}")
    print("end of main coroutine")
    
asyncio.run(main())