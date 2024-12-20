
[Asyncio in Python](https://www.youtube.com/watch?v=Qb9s3UiMSTA)

- Start tasks at tasks B, C, D even if task A isn't finished yet. 
- Handle multiple tasks simultaneously, making it more efficient for opertations with waiting times like I/O. 
- Asyncio: Use for tasks that wait alot, like network requests or reading files. Handle many tasks concurrently without much CPU. More efficient and responsive when you're waiting on many tasks. 

- Threads: Use for tasks that may need to wait AND also share data. Useful for IO bound tasks that are CPU light. 
- Processes: Use for tasks with intensive computations, CPU heavy tasks, each process operates independently, maximizing CPU usage by running in parallel across multiple cores. 

# concepts 

Event Loop

Core that manages and distributes tasks. Central hub with tasks circling around it waiting for their turn to be executed. Task is executed immediately or paused. When paused, the task steps aside and lets a different task to start. 

Coroutine function 

Async function that returns a coroutine object. 

Coroutine object must be awaited to be executed. 

Tasks

Tasks do not use multiple cpu cores, they don't execute at the exact same time. 

Tasks attempt to do productive work when another tassk is blocked. 

The event loop coordinates switching between tasks. 

Future

A promise of an eventual result or value of a future object. 