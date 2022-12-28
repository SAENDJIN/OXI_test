import allure
from playwright.sync_api import Playwright
from usefull_tool.email_generator import random_email
from usefull_tool.new_phone_generator import random_phone, random_number_two
from usefull_tool.birtday_generator import random_date
from usefull_tool.email_log import add_email_to_txt
from usefull_tool.name_generator import first_name, second_name
from usefull_tool.random_postal_and_address import random_postal, random_address, random_city
from usefull_tool.datetime_screenshot import screenshot_name


class RegistrationDeposit:
    """Test user flow registration -> fill user info -> deposit -> open new page with any deposit method"""

    @allure.step
    def __init__(self, playwright: Playwright):
        """Configure browser to start autotest"""
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://oxicasino.io/de/")

    @allure.step
    def registration_form(self):
        """Fill registration inputs"""
        self.page.locator("button:has-text(\"Registrieren\")").first.click()
        self.page.locator("[placeholder=\"E-Mail\"]").fill(random_email)
        add_email_to_txt()
        self.page.locator("[placeholder=\"Passwort\"]").fill("ilimem31")
        self.page.locator(
            "label:has-text(\"Ich bin über 18 Jahre alt und stimme den AGB und Datenschutzerklärung zu\") span").nth(
            1).click()
        self.page.locator("button:has-text(\"Schließen Sie die Registrierung ab\")").click()

    @allure.step
    def trigger_profile_input(self):
        """Made moves to get profile placeholder"""
        self.page.wait_for_url("https://oxicasino.io/de/wallet/deposit")
        self.page.locator("li:nth-child(18) > .paymentList__img").click()
        self.page.locator("button:has-text(\"Einzahlen\")").click()

    @allure.step
    def profile_info_fill(self):
        """Fill user profile info"""
        self.page.locator("[placeholder=\"Telefonnummer\"]").fill(random_phone)
        self.page.locator("[placeholder=\"Name\"]").fill(first_name)
        self.page.locator("[placeholder=\"Nachname\"]").fill(second_name)
        self.page.locator("[placeholder=\"Geburtsdatum\"]").fill(random_date)
        self.page.locator("[placeholder=\"Stadt\"]").fill(random_city)
        self.page.locator("[placeholder=\"Adresse\"]").fill(random_address + " " + str(random_number_two))
        self.page.locator("[placeholder=\"Postleitzahl\"]").fill(random_postal)
        self.page.locator(".pseudoRadio__wrap").first.click()
        self.page.locator("text=Speichern").click()

    @allure.step
    def deposit_to_redirect(self):
        """steps to open new window"""
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
