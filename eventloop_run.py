import asyncio

loop = asyncio.new_event_loop()
print(loop)
loop.run_until_complete(asyncio.sleep(8))