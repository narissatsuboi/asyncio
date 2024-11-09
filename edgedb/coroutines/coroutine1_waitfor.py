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


# wrap coroutine in a wait_for with a timeout
timeout = 10
asyncio.run(asyncio.wait_for(keep_printing(), timeout))

#   File "C:\Python312\Lib\asyncio\base_events.py", line 687, in run_until_complete
#     return future.result()
#            ^^^^^^^^^^^^^^^
#   File "C:\Python312\Lib\asyncio\tasks.py", line 519, in wait_for
#     async with timeouts.timeout(timeout):
#   File "C:\Python312\Lib\asyncio\timeouts.py", line 115, in __aexit__
#     raise TimeoutError from exc_val
# TimeoutError

# ^^^ tldr: async function did not finish executing before the timeout
