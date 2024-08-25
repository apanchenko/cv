from collections.abc import AsyncIterator
from prisma import Prisma


async def get_db() -> AsyncIterator[Prisma]:
    """Get database."""
    db = Prisma(auto_register=True)
    await db.connect()

    yield db

    await db.disconnect()
