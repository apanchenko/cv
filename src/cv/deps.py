from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from prisma import Prisma


@asynccontextmanager
async def with_db() -> AsyncIterator[Prisma]:
    """Get database."""
    db = Prisma()
    await db.connect()

    try:
        yield db
    finally:
        await db.disconnect()


async def get_db() -> AsyncIterator[Prisma]:
    """Get database."""
    async with with_db() as db:
        yield db
