import asyncio

shared_resource = 0

# ensure no two coroutines have access to this
# resource at the same time
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    # acquire the lock with the async context manager
    # checks if any other coroutine is using the lock
    # if it is, it waits, if not, goes into block of code
    async with lock: 
        # critical section modification
        print(f"resource before modification: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(1) # sim IO operation
        print(f"resource after modification: {shared_resource}")
        # end crtical section modification
        
async def main():
    # create 5 instances of the coroutine
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))
    
asyncio.run(main())