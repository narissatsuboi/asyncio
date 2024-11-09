import asyncio
import datetime

loop = asyncio.new_event_loop()

# Executing <TimerHandle when=172436.765 hog() at asyncio\hog.py:7 created at g:\My Drive\source\code\asyncio\hog.py:27> took 4.781 seconds
loop.set_debug(True)

def hog():
    sum = 0
    for i in range(10_000):
        for j in range(10_000):
            sum += j
    return sum 

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
loop.call_later(delay=15,callback=hog)

loop.call_later(delay=20, callback=loop.stop)
loop.run_forever()