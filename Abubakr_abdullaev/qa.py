import pytest
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=450, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.set_default_navigation_timeout(20000)
    page.set_default_timeout(20000)
    page.goto("https://kassa-dev.smartpos.uz")
    if "Smartphos Web-Kassa" in page.title():
        page.locator("//*[@id='username']").fill("905439771")
        page.locator("//*[@id='password']").fill("832145")
        page.locator("//*[@id='remember']").check()
        page.locator("//*[@id='submit']").click()
        time.sleep(3)

    browser.close()