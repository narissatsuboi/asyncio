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
    """Coroutine uses taskgroup to execute multiple tasks concurrently and store results in a list. 
    """
    
    tasks = []
    
    # async with is an asynchronous context manager
    # it gives access to the tg and blocks until
    # all tasks executed
    async with asyncio.TaskGroup() as tg:
        for i, delay in enumerate([2, 1, 3], start=1):
            task = tg.create_task(sim_fetch_with_delay(delay, i))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")
        
asyncio.run(main())