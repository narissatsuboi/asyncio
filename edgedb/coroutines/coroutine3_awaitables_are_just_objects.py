import asyncio
import datetime


def print_now():
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    """Infinite loop to print datetime at an interval"""
    sleep_time = 0.50  # MINIMUM blocking time, no exact guarantee.
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(
            sleep_time
        )  # event loop can switch to execute something else


async def async_main() -> None:
    """Entrypoint to running async behavior"""
    timeout = 10

    kp = keep_printing("Hey")  # store coroutine
    waiter = asyncio.wait_for(kp, timeout)  # store awaitable

    try:
        await waiter  # await on awaitable (run coroutine)
    except asyncio.TimeoutError:
        print("oops, timeout error")


asyncio.run(async_main())
