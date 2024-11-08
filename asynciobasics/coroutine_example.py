import asyncio

# coroutine function
async def main():
    """ Returns a coroutine object """
    print("start of main coroutine")

# pass the coroutine object to .run
# to start the event loop
asyncio.run(main()) 