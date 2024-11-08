import asyncio 


async def access_resource(semaphore, resource_id):
    async with semaphore:
        print(f"accessing resource {resource_id}")
        await asyncio.sleep(1)
        print(f"releasing resource {resource_id}")

async def main():
    # semaphore allows multiple coroutines access to the 
    # same resource at the same time
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))
    
asyncio.run(main())