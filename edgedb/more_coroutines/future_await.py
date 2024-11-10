import asyncio
from typing import Awaitable


async def get_result(awaitable: Awaitable) -> str:
    try:
        result = await awaitable
    except Exception as e:
        print("oop! found an exception of", type(e))
        return
    except asyncio.CancelledError as c:
        print("oop, future was cancelled! found an exception of", type(c))
    else:
        print(result)


# init an event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


# # set the result after the delay and await
# fut = asyncio.Future()
# loop.call_later(5, fut.set_result, "this is the result")
# loop.run_until_complete(future=get_result(fut))

# # set an exception after the delay and await
# fut = asyncio.Future()
# loop.call_later(5, fut.set_exception, ValueError("problem encountered"))
# loop.run_until_complete(future=get_result(fut))

# # cancel the future, asyncio.exceptions.CancelledError is not handled
# # cancel exception is a subclass BaseException, not Exception
# fut = asyncio.Future()
# loop.call_later(5, fut.cancel)  # asyncio.exceptions.CancelledError
# loop.run_until_complete(future=get_result(fut))

# # multiple coroutines can await the same future
# fut = asyncio.Future()
# loop.call_later(5, fut.set_result, "final result")
# loop.run_until_complete(
#     asyncio.gather(get_result(fut), get_result(fut), get_result(fut))
# )


# add a callback(s) directly to a future
# callback(s) will be called when the future is done
def callback(fut: asyncio.Future) -> None:
    print("called by", fut)


# callbacks run when the event loop is started, not when the result is set
fut = asyncio.Future()
fut.add_done_callback(callback)
fut.add_done_callback(lambda fut: loop.stop())
fut.set_result("setting the result")  # schedules the callbacks
loop.run_forever()  # called by <Future finished result='setting the result'>
