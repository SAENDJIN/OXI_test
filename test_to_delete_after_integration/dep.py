# andrii.qa31+autotest.de@gmail.com
# ilimem31

from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oxicasino.io/de/")
    # ---------------------
    page.get_by_role("button", name="Einloggen").click()
    page.get_by_placeholder("Benutzername").click()
    page.get_by_placeholder("Benutzername").fill("andrii.qa31+autotest.de@gmail.com")
    page.get_by_placeholder("Passwort").click()
    page.get_by_placeholder("Passwort").fill("ilimem31")
    # ---------------------
    page.locator("form:has-text(\"Benutzername popup_login.field_incorrect Passwort popup_login.field_incorrect Pa\")").get_by_role("button", name="Einloggen").click()
    page.get_by_role("button", name="€ 0 Einzahlung").click()
    page.wait_for_url("https://oxicasino.io/de/wallet/deposit")
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
