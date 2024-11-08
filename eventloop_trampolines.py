import asyncio
import datetime

loop = asyncio.new_event_loop()

def print_now():
    print(datetime.datetime.now())
    
def trampoline(name: str="") -> None:
    """Registers itself back on the event loop after
    completing one tick"""
    print(name, end=" ")
    print_now() 
    loop.call_later(0.5, trampoline, name)

loop.call_soon(trampoline, "First")
loop.call_soon(trampoline, "Second")
loop.call_soon(trampoline, "Third")

loop.call_later(delay=8, callback=loop.stop)
loop.run_forever()