from os import getcwd
from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto(f'file://{getcwd()}/cv.html')
    page.pdf(
        format='A4',
        path='Anton Panchenko CV 2024.pdf',
    )
    browser.close()

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
