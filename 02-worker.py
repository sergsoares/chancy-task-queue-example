import os
import asyncio
from chancy import Chancy, Worker
from chancy.plugins.api import Api
from chancy.plugins.api.auth import SimpleAuthBackend

chancy = Chancy(
    os.getenv('CHANCY_DB_URL'),
    plugins=[
        Api(
            port=int(os.getenv('CHANCY_API_PORT', 8000)),
            host=os.getenv('CHANCY_API_HOST', 'localhost'),
            debug=os.getenv('CHANCY_DEBUG', 'false').lower() == 'true',
            authentication_backend=SimpleAuthBackend({"admin": "admin"}),
            allow_origins=['*']
        )
    ]
)

async def main():
    async with chancy:
        async with Worker(chancy) as worker:
            await worker.wait_for_shutdown()

if __name__ == "__main__":
    asyncio.run(main())