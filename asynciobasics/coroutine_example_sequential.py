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
    coroutine_obj_1 = sim_fetch_with_delay(2, 1)
    coroutine_obj_2 = sim_fetch_with_delay(2, 2)
    
    result_1 = await coroutine_obj_1
    print(f"received result: {result_1}")
    result_2 = await coroutine_obj_2
    print(f"received result: {result_2}")
    print("end of main coroutine")
    
asyncio.run(main())