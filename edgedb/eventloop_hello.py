import asyncio

def hello_world(loop):
    """A callback to print and stop the event loop"""
    print('Hello World')
    loop.stop()

loop = asyncio.new_event_loop()

# schedule a call to hello_world
loop.call_soon(hello_world, loop)

try:
    loop.run_forever()
finally:
    loop.close()