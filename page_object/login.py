from playwright.sync_api import Playwright
import time


class LoginDeposit:
    """Test user flow login -> deposit -> open new page with any deposit method"""

    def __init__(self, playwright: Playwright):
        """Configure browser to start autotest"""
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://oxicasino.io/de/")

    def login_form(self):
        """Fill login inputs"""
        self.page.get_by_role("button", name="Einloggen").click()
        self.page.get_by_placeholder("Benutzername").click()
        self.page.get_by_placeholder("Benutzername").fill(
            "andrii.qa31+autotest.de@gmail.com")  # Solve what email to use
        self.page.get_by_placeholder("Passwort").click()
        self.page.get_by_placeholder("Passwort").fill("ilimem31")

    def go_to_deposit(self):
        """Redirect to page with deposit methods"""
        self.page.locator(
            "form:has-text(\"Benutzername popup_login.field_incorrect Passwort popup_login.field_incorrect Pa\")") \
            .get_by_role("button", name="Einloggen").click()
        self.page.get_by_role("button", name="€ 0 Einzahlung").click()
        self.page.wait_for_url("https://oxicasino.io/de/wallet/deposit")

    def choose_payment_method(self):
        """Choose payment method"""
        # test with this code (maybe should codegen)
        self.page.locator(".paymentList__img").first.click()
        self.page.get_by_role("button", name="€ 30.00").click()
        # self.page.get_by_role("button", name="Einzahlen").click()

    def check_new_window(self):
        """Assertion new window is opened"""
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("button", name="Einzahlen").click()
        page1 = popup_info.value
        time.sleep(2)
        current_url = page1.url(timeout= )
        self.page.wait_for_url(current_url)
        page1.goto(current_url)

        return

    def close(self):
        """End of test"""
        time.sleep(5)
        self.context.close()
        self.browser.close()
