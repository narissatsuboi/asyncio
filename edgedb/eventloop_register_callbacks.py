import asyncio
import datetime

def print_now():
    print(datetime.datetime.now())

loop = asyncio.new_event_loop()

loop.call_soon(print_now)  # schedule/register
loop.call_soon(print_now)  # schedule/registser another

# run the event loop
loop.run_until_complete(asyncio.sleep(5))