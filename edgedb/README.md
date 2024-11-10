[1. The Async Ecosystem](https://www.youtube.com/watch?v=Xbl7XjFYsN4&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB)

Time to interact: Metric of time from user action to appearance of interaction from UI. Minimize by splitting webpage into parts that can load independently. 

Don't block the foreground with synchronous code, only do long running operations in the background, asynchronously.

IO: Waiting for external resources. 

asyncioIO goal: Maximize the usage of a single thread by handling IO asynchronously and by enabling concurrent code with coroutines.

ThreadLocal Storage: Global vars only seen by the current thread. Passed to each coroutine. Cumbersome/ugly.

Context Variables: Replace ThreadLocal Storage.

[2. The Event Loop](https://www.youtube.com/watch?v=E7Yn5biBZ58&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB&index=2)

Event loop is calling callbacks one by one.

Unix uses selector event loops. Windows uses proactor event loops. 

unix_events selects the appropriate selector:
- Kqueue
- epoll
- /dev/poll
- poll
- select 

Python creates default event loop in the main thread only. 

New threads / secondary threads / work threads need to have a new event loop with the selector manually. 

_run_once
- Call all ready callbacks
- Poll for IO
- Schedule resulting callbacks
- Schedule 'call_later' callbacks

In production, should be running uvloop. 

[3. Using Coroutines](https://www.youtube.com/watch?v=-CzqsgaXUM8)

using async def compiles the function as asynchronous

async function: Function that creates a coroutine when called. Define with async def. Can use await inside the function. The function itself is not awaitable.

coroutine: Object created by calling an async function. It is awaitable, but only once. Low level building block.

awaitable: Any object that can be awaited on. Await blocks further execution in an async function, it yields execution back to asyncio so it can switch to something else.

Task: Wrapper for coroutines, managed by asyncio framework. 

futures

IF a timeout occurs, whatever we were waiting for is cancelled. A TimeoutError is raised. 

Set these flags to detect unawaited awaitables in your code. 
- PYTHONASYNCIODEBUG=1
- PYTHONTRACEMALLOC=1 (local perf penality with this one)


[4. Coroutines Under the Hood](https://www.youtube.com/watch?v=1LTHbmed3D4&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB&index=4)

future: object serving as a container for a result we don't have yet, but will in the future. 

cancel a future: don't need or cannot accept the result anymore. 

fair scheduling, first in first out. 

coroutines work by running callbacks. they run a single step of execution as a callback, and if theres any execution left, they use the trampoline pattern to schedule themselves back on the event loop.

task is the gateway to coroutine computation. tasks are where the trampoline pattern is used, and coroutine is split into multiple discrete steps. 

in the real world, there are many tasks happening at the same time, but each one runs a short amount a code until it encounters an await, and then schedules itself back on the event loop.

network latency >>> computational cost of event loop and splitting coroutines into small tasks

green threading / cooperative computation threads / background threads

if a green thread runs too long, it can still bottleneck the event loop

avoid blocking calls within async functions

handle thousands of clients on a single asyncio main thread