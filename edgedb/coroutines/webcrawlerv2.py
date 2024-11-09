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

    # create background task that runs only when awaiting
    asyncio.create_task(algo(url), name=url)
    todo.add(url)
    start = time()
    while len(todo):
        print(f"{len(todo)}: " + ", ".join(sorted(todo))[-38:])
        await asyncio.sleep(0.5)
    end = time.time()
    print(f"Took {int(end - start)}" + " seconds")


async def crawl2(prefix: str, url: str = "") -> None:
    url = url or prefix
    client = httpx.AsyncClient()
    try:
        res = await client.get(url)
    finally:
        await client.aclose()

    for line in res.text.splitlines():
        if line.startswith(prefix):
            todo.add(line)
            # found the next line to crawl
            # create a background task without blocking!
            asyncio.create_task(coro=crawl2(prefix, line), name=line)
    todo.discard(url)


asyncio.run(progress(addr, crawl2))
