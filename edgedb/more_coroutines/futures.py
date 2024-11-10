import asyncio

# init an event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# init a future
fut = asyncio.Future()

print(fut.done(), "- future is done?")  # False
print(fut.cancelled(), "- future is cancelled?")  # False

# get a result?
try:
    fut.result()
except asyncio.InvalidStateError as e:
    print(".result() throws b/c futures result is not available yet")
    print(e)

# set the result
fut.set_result("Future has a result")

# result is available
print(fut.result())
