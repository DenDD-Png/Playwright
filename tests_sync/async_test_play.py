from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://ya.ru")
        await page.screenshot(path="../screenshot/ya.png")
        await browser.close()

asyncio.run(main())
