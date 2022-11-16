from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oxicasino.io/de/")
    # ---------------------
    page.get_by_role("button", name="Registrieren").click()
    page.get_by_placeholder("E-Mail").click()
    page.get_by_placeholder("E-Mail").fill("andrii.qa31+test.de.auto@gmail.com")
    page.get_by_placeholder("Passwort").click()
    page.get_by_placeholder("Passwort").fill("ilimem31")
    page.locator(
        "label:has-text(\"Ich bin über 18 Jahre alt und stimme den AGB und Datenschutzerklärung zu\") span").nth(
        1).click()
    page.get_by_role("button", name="Schließen Sie die Registrierung ab").click()
    # ---------------------
    page.wait_for_url("https://oxicasino.io/de/wallet/deposit")
    page.locator(".paymentList__img").first.click()
    page.get_by_role("button", name="€ 30.00").click()
    page.get_by_role("button", name="Einzahlen").click()
    # ---------------------
    page.get_by_placeholder("Telefonnummer").click()
    page.get_by_placeholder("Telefonnummer").fill("+4 (930) 674-06-06 65")  # Generate new phone every time
    page.get_by_role("textbox", name="Name incorrect_field").click()
    page.get_by_role("textbox", name="Name incorrect_field").fill("FirstName")
    page.get_by_placeholder("Nachname").click()
    page.get_by_placeholder("Nachname").fill("LastName")
    page.get_by_placeholder("Geburtsdatum").click()
    page.get_by_placeholder("Geburtsdatum").fill("12.12.1995")
    page.get_by_placeholder("Stadt").click()
    page.get_by_placeholder("Stadt").fill("Leun")
    page.get_by_placeholder("Adresse").click()
    page.get_by_placeholder("Adresse").fill("Wetzlarer Strasse 77")  # maybe random number at the end every time
    page.get_by_placeholder("Postleitzahl").click()
    page.get_by_placeholder("Postleitzahl").fill("35638")
    page.get_by_label("Männlich").check()
    # ---------------------
    page.get_by_role("button", name="Speichern").click()
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Einzahlen").click()
    page1 = popup_info.value
    page.wait_for_url("https://onetouch.astropay.com/deposit/SchTD7fCeOpIG2yyfooazEXRX7M5lksI5r2iWZge")
    page1.goto("https://onetouch.astropay.com/deposit/checkout/SchTD7fCeOpIG2yyfooazEXRX7M5lksI5r2iWZge")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
