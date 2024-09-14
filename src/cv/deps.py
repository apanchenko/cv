from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from playwright.async_api import Page, async_playwright

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


async def get_page() -> AsyncIterator[Page]:
    """Get new page."""
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        try:
            yield page
        finally:
            await browser.close()
