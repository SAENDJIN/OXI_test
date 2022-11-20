from playwright.sync_api import Playwright
from usefull_tool.email_generator import random_email
from usefull_tool.new_phone_generator import random_phone, random_number_two
from usefull_tool.birtday_generator import random_date


class RegistrationDeposit:
    """Test user flow registration -> fill user info -> deposit -> open new page with any deposit method"""

    def __init__(self, playwright: Playwright):
        """Configure browser to start autotest"""
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://oxicasino.io/de/")

    def registration_form(self):
        """Fill registration inputs"""
        self.page.get_by_role("button", name="Registrieren").click()
        self.page.get_by_placeholder("E-Mail").click()
        self.page.get_by_placeholder("E-Mail").fill(random_email)  # Generate random email every time (PASS)
        # it depends on what we choose json or list. Add append to it
        self.page.get_by_placeholder("Passwort").click()
        self.page.get_by_placeholder("Passwort").fill("ilimem31")
        self.page.locator(
            "label:has-text(\"Ich bin über 18 Jahre alt und stimme den AGB und Datenschutzerklärung zu\") span").nth(
            1).click()
        self.page.get_by_role("button", name="Schließen Sie die Registrierung ab").click()

    def trigger_profile_input(self):
        """Made moves to get profile placeholder"""
        self.page.wait_for_url("https://oxicasino.io/de/wallet/deposit")
        self.page.locator(".paymentList__img").first.click()
        self.page.get_by_role("button", name="€ 30.00").click()
        self.page.get_by_role("button", name="Einzahlen").click()

    def profile_info_fill(self):
        """Fill user profile info"""
        self.page.get_by_placeholder("Telefonnummer").click()
        self.page.get_by_placeholder("Telefonnummer").fill(random_phone)  # Generate new phone every time (PASS)
        self.page.get_by_role("textbox", name="Name incorrect_field").click()  # unknown step (maybe delete)
        self.page.get_by_role("textbox", name="Name incorrect_field").fill("FirstName")
        self.page.get_by_placeholder("Nachname").click()
        self.page.get_by_placeholder("Nachname").fill("LastName")
        self.page.get_by_placeholder("Geburtsdatum").click()  # Birthday Date
        self.page.get_by_placeholder("Geburtsdatum").fill(random_date)  # Generate random birthday date (DONE)
        self.page.get_by_placeholder("Stadt").click()
        self.page.get_by_placeholder("Stadt").fill("Leun")  # City  (maybe crate list with city and take randomly)
        self.page.get_by_placeholder("Adresse").click()  # Address (maybe crate list with address and take randomly)
        self.page.get_by_placeholder("Adresse").fill(
            "Wetzlarer Strasse " + str(random_number_two))  # maybe random number at the end every time DONE
        self.page.get_by_placeholder("Postleitzahl").click()  # Postal code
        # (maybe crate list with postal code and take randomly)
        self.page.get_by_placeholder("Postleitzahl").fill("35638")
        self.page.get_by_label("Männlich").check()

    def deposit_to_redirect(self):
        """steps to open new window"""
        self.page.get_by_role("button", name="Speichern").click()
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("button", name="Einzahlen").click()
        page1 = popup_info.value
        self.page.wait_for_url("https://onetouch.astropay.com/deposit/SchTD7fCeOpIG2yyfooazEXRX7M5lksI5r2iWZge")
        page1.goto("https://onetouch.astropay.com/deposit/checkout/SchTD7fCeOpIG2yyfooazEXRX7M5lksI5r2iWZge")
        # maybe problem here

    def check_new_window(self):
        """Check result of test"""
        # Add
        return

    def close(self):
        """End of test"""
        self.context.close()
        self.browser.close()
