[The Async Ecosystem](https://www.youtube.com/watch?v=Xbl7XjFYsN4&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB)

Time to interact: Metric of time from user action to appearance of interaction from UI. Minimize by splitting webpage into parts that can load independently. 

Don't block the foreground with synchronous code, only do long running operations in the background, asynchronously.

IO: Waiting for external resources. 

asyncioIO goal: Maximize the usage of a single thread by handling IO asynchronously and by enabling concurrent code with coroutines.