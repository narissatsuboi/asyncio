import asyncio
import datetime
import inspect


def print_now():
    print(datetime.datetime.now())


async def print3times() -> None:
    for _ in range(3):
        print_now()
        await asyncio.sleep(0.1)


# async functions are not awaitable
print(type(print3times), "-> print3times type")  # <class 'function'>
print(inspect.isawaitable(print3times), "-> print3times is awaitable?")

# coroutines are awaitable
coro1 = print3times()
coro2 = print3times()
print(type(coro1), "-> coroutine of print3times type")  # <class 'coroutine'>
print(inspect.isawaitable(coro1), "-> coroutine of print3times is awaitable?")

# sequentially runs coroutines
asyncio.run(coro1)
asyncio.run(coro2)

# cannot run a coroutine again
try:
    asyncio.run(coro1)
except RuntimeError as e:
    print(e)  # "cannot reuse already awaited coroutine"
