import asyncio
from textwrap import indent


async def example(count: int) -> str:
    """creates an await chain/yield from chain"""
    print(indent(count), "Before the first await")
    await asyncio.sleep(0)
    print(indent(count), "After the first await")
    if count == 0:
        return "result"
    for i in range(count):
        print(indent(count), "Before await inside loop iteration", i)
        await asyncio.sleep(i)
        print(indent(count), "After await inside loop iteration", i)
    print(indent(count), f"Before await on example({count - 1})")
    return await example(count - 1)


class TraceStep(asyncio.tasks._PyTask):
    """Create wrapper around __step to add logging"""

    def _Task__step(self, exc=None):
        # before await
        print(f"<step name={self.get_name} done={self.done()}>")
        result = super()._Task__step(exc=exc)
        # after await
        print(f"<step name={self.get_name} done={self.done()}>")


# init an event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.set_task_factory(lambda loop, coro: TraceStep(example(0), loop=loop))
