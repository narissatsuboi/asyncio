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
    """Coroutine uses gather to execute multiple tasks concurrently and store results in a list. 
    """
    
    # gather doesn't cancel other coroutines if one fails
    # no error handling
    results = await asyncio.gather(sim_fetch_with_delay(2,1), sim_fetch_with_delay(3,2), sim_fetch_with_delay(1,3))
    
    for result in results:
        print(f"Received result: {result}")
        
asyncio.run(main())