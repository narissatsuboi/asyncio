import asyncio

async def sim_fetch_with_delay(delay: int, id: int):
    """Coroutine that simulates a IO operation with a delay
    via sleep. 
    Args:
        delay (int): seconds to wait
    """
    print(f"fetching data with a delay of {delay} seconds and id {id}")
    await asyncio.sleep(delay) 
    print("data fetched for id:", id)
    return {"data": "some data", "id": id}

async def main():
    """Coroutine that awaits two coroutine objects sequentially. 
    
    4 seconds to execute.
    """

    task_1 = asyncio.create_task(sim_fetch_with_delay(2,1))
    task_2 = asyncio.create_task(sim_fetch_with_delay(3,2))
    task_3 = asyncio.create_task(sim_fetch_with_delay(1,3))
    
    result_1 = await task_1
    print(f"received result: {result_1}")
    result_2 = await task_2
    print(f"received result: {result_2}")
    result_3 = await task_3
    print(f"received result: {result_3}")
    print("end of main coroutine")
    
asyncio.run(main())