from pathlib import Path

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    """Start browser and save to pdf."""
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto(f'file://{Path.cwd()}/cv.html')
    page.pdf(
        format='A4',
        path='Anton Panchenko CV 2024.pdf',
    )
    browser.close()

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
