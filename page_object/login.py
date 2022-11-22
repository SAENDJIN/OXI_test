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
        """Fill login inputs"""
        self.page.get_by_role("button", name="Einloggen").click()
        self.page.get_by_placeholder("Benutzername").fill(
            "andrii.qa31+autotest.de@gmail.com")  # Solve what email to use
        self.page.get_by_placeholder("Passwort").fill("ilimem31")

    def go_to_deposit(self):
        """Redirect to page with deposit methods"""
        self.page.locator("div[role=\"dialog\"] button:has-text(\"Einloggen\")").click()

        self.page.get_by_role("button", name="€ 0 Einzahlung").click()
        self.page.wait_for_url("https://oxicasino.io/de/wallet/deposit")

    def choose_payment_method(self):
        """Choose payment method"""
        self.page.locator("li:nth-child(18) > .paymentList__img").click()
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("button", name="Einzahlen").click()
        page1 = popup_info.value
        page1.close()

    def check_new_window(self):
        """Assertion new window is opened"""
        text_header_popup = self.page.locator("//html/body/div[4]/div[1]/div/div/div/div/div/h2").text_content()
        return "Warten auf die Zahlung" in text_header_popup

    def close(self):
        """End of test"""
        self.context.close()
        self.browser.close()

