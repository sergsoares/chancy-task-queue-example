import asyncio
import os
from jobs import fibonacci, hello_world
from chancy import Chancy

chancy = Chancy(
    os.getenv('CHANCY_DB_URL')
)

async def main():
    await chancy.push(hello_world.job.with_kwargs(name="Async job").with_queue('another'))
    print("Created sync job into another queue")

if __name__ == "__main__":
    chancy.sync_push(fibonacci.job.with_kwargs(n=12))
    print("Created sync job into default queue")

    chancy.sync_push(fibonacci.job.with_kwargs(n=23).with_queue('custom'))
    print("Created sync job into custom queue")
    asyncio.run(main())