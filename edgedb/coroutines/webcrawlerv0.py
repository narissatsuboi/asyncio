import httpx
import asyncio


async def crawl0(prefix: str, url: str = "") -> None:
    """
    Issues
    1. Separate reporting progress task from backend task
    2. await crawl0 creates recursive call
    3. await crawl0 creates another blocking call
    """
    url = url or prefix
    print(f"crawling {url}")
    client = httpx.AsyncClient()
    try:
        res = await client.get(url)
    finally:
        await client.aclose()

    for line in res.text.splitlines():
        if line.startswith(prefix):
            await crawl0(prefix, line)


asyncio.run(crawl0("https://langa.pl/crawl/"))
