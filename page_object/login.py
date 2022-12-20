from playwright.sync_api import Playwright
import allure
from usefull_tool.datetime_screenshot import screenshot_name

class LoginDeposit:
    """Test user flow login -> deposit -> open new page with any deposit method"""

    def __init__(self, playwright: Playwright):
        """Configure browser to start autotest"""
        self.browser = playwright.chromium.launch(headless=False, timeout=1500)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://oxicasino.io/de/")

    @allure.step
    def login_form(self):
        """Fill login inputs"""
        self.page.locator("button:has-text(\"Einloggen\")").first.click()
        self.page.locator("[placeholder=\"Benutzername\"]").fill("andrii.qa31+autotest.de@gmail.com")
        self.page.locator("[placeholder=\"Passwort\"]").fill("ilimem31")

    @allure.step
    def go_to_deposit(self):
        """Redirect to page with deposit methods"""
        self.page.locator("div[role=\"dialog\"] button:has-text(\"Einloggen\")").click()

        self.page.locator("text=€ 0Einzahlung").click()
        self.page.wait_for_url("https://oxicasino.io/de/wallet/deposit")

    @allure.step
    def choose_payment_method(self):
        """Choose payment method"""
        self.page.locator("li:nth-child(18) > .paymentList__img").click()
        with self.page.expect_popup() as popup_info:
            self.page.locator("button:has-text(\"Einzahlen\")").click()
        page1 = popup_info.value
        page1.close()

    @allure.step
    def check_new_window(self):
        """Assertion new window is opened"""
        text_header_popup = self.page.locator("text=Warten auf die Zahlung").text_content()
        try:
            assert "Warten auf die Zahlung" in text_header_popup
        except AssertionError:
            # Take a screenshot and attach it to the Allure report
            screenshot = self.page.screenshot()
            allure.attach(screenshot, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            # Re-raise the AssertionError to fail the test
            raise

    @allure.step
    def close(self):
        """End of test"""
        self.context.close()
        self.browser.close()
