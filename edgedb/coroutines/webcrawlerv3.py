from datetime import time
from typing import Callable, Coroutine
import httpx
import asyncio

addr = "https://langa.pl/crawl/"
todo = set()


async def progress(
    url: str,
    algo: Callable[..., Coroutine],
) -> None:
    """Stores created task in todo set and processes them until all are completed."""
    # create and store background task that runs only when awaiting
    task = asyncio.create_task(algo(url), name=url)
    todo.add(task)
    start = time()
    while len(todo):
        # done contains Futures that are completed
        # pending contains Futures that are not completed
        # NO TimeoutError is thrown!!!! Sets are updated every 'timeout' seconds.
        done, _pending = await asyncio.wait(fs=todo, timeout=0.5)

        # remove the completed tasks from to todo set
        todo.difference_update(done)

        # get all the remaining task names
        urls = (t.get_name() for t in todo)
        print(f"{len(todo)}: " + ", ".join(sorted(urls))[-75:])
    end = time.time()
    print(f"Took {int(end - start)}" + " seconds")


async def crawl3(prefix: str, url: str = "") -> None:
    url = url or prefix
    client = httpx.AsyncClient()
    try:
        res = await client.get(url)
    finally:
        await client.aclose()

    for line in res.text.splitlines():
        if line.startswith(prefix):
            # found the next line to crawl
            # create a background task without blocking!
            task = asyncio.create_task(coro=crawl3(prefix, line), name=line)
            todo.add(task)


asyncio.run(progress(addr, crawl3))
