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
    """wait for waits on gather, upon timeout, gather coroutine is cancelled
    and propogated cancellation to incomplete awaitables"""
    try:
        await asyncio.wait_for(
            fut=asyncio.gather(
                keep_printing("First"),
                keep_printing("Second"),
                keep_printing("Third"),
            ),
            timeout=5.0,
        )
    except TimeoutError:
        print("oops timeout error")
        # gather coroutine has been cancelled


asyncio.run(async_main())
