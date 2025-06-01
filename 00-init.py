import os
import asyncio
from chancy import Chancy, Queue
from chancy.plugins.api import Api
from chancy.plugins.api.auth import SimpleAuthBackend

chancy = Chancy(
    os.getenv('CHANCY_DB_URL', "postgresql://postgres:postgres@localhost:5430/postgres"),
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
        await chancy.migrate()
        await chancy.declare(Queue("default"))
        await chancy.declare(Queue("custom"))
        await chancy.declare(Queue("another"))
        print("Migrated and created queues")

if __name__ == "__main__":
    asyncio.run(main())