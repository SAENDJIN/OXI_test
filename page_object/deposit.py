from playwright.sync_api import Playwright


class LoginDeposit:
    """Test user flow login -> deposit -> open new page with any deposit method"""

    def __init__(self, playwright: Playwright):
        """Configure browser to start autotest"""
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://oxicasino.io/de/")

    def login_form(self):
        self.page.get_by_role("button", name="Einloggen").click()
        self.page.get_by_placeholder("Benutzername").click()
        self.page.get_by_placeholder("Benutzername").fill("andrii.qa31+autotest.de@gmail.com")  # Solve what email to use
        self.page.get_by_placeholder("Passwort").click()
        self.page.get_by_placeholder("Passwort").fill("ilimem31")

    def go_to_deposit(self):
        self.page.locator(
            "form:has-text(\"Benutzername popup_login.field_incorrect Passwort popup_login.field_incorrect Pa\")")\
            .get_by_role("button", name="Einloggen").click()
        self.page.get_by_role("button", name="€ 0 Einzahlung").click()
        self.page.wait_for_url("https://oxicasino.io/de/wallet/deposit")

    def choose_payment_method(self):
        # add
    def check_new_window(self):
        # add
    def close(self):
        self.context.close()
        self.browser.close()
