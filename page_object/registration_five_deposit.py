import allure
from playwright.sync_api import Playwright
from usefull_tool.email_generator import random_email
from usefull_tool.new_phone_generator import random_phone, random_number_two
from usefull_tool.birtday_generator import random_date
from usefull_tool.email_log import add_email_to_txt
from usefull_tool.name_generator import first_name, second_name
from usefull_tool.random_postal_and_address import random_postal, random_address, random_city
from usefull_tool.datetime_screenshot import screenshot_name


class RegistrationDepositFiveMethod:
    """
    Test user flow registration -> fill user info -> deposit ->
    (bank_uberweisung_black / bank_uberweisung_white / visa / mastercard_paygate / mastercard_payment_service)
    """

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
    def payment_bank_uberweisung_black(self):
        """Open new deposit window with bank_uberweisung_black and try to find element"""
        self.page.locator(".paymentList__img").first.click()
        self.page.locator("[placeholder=\"\\30 \"]").fill("20")
        with self.page.expect_popup() as popup_info:
            self.page.locator("button:has-text(\"Einzahlen\")").click()
        page1 = popup_info.value
        bank_uberweisung_black = page1.locator("//html/body/div/main/div/aside/section/div[1]/div/div/div/div/h2[2]") \
            .text_content()

        assert "€20.00" in bank_uberweisung_black
        page1.close()

    @allure.step
    def payment_bank_uberweisung_white(self):
        """Open new deposit window with bank_uberweisung_white and try to find element"""

        self.page.locator("li:nth-child(5) > .paymentList__img").click()
        self.page.locator("[placeholder=\"\\30 \"]").fill("20")
        with self.page.expect_popup() as popup_info:
            self.page.locator("button:has-text(\"Einzahlen\")").click()
        page2 = popup_info.value
        bank_uberweisung_white = page2.locator("text=Confirm and pay 20.00 EUR") \
            .text_content()

        assert "Confirm and pay 20.00 EUR" in bank_uberweisung_white
        page2.close()

    # @allure.step
    # def payment_visa(self):
    #     """Open new deposit window with visa and try to find element"""
    #     self.page.locator("li:nth-child(4) > .paymentList__img").click()
    #     self.page.locator("[placeholder=\"\\30 \"]").fill("20")
    #     with self.page.expect_popup() as popup_info:
    #         self.page.locator("button:has-text(\"Einzahlen\")").click()
    #     page3 = popup_info.value
    #     visa = page3.locator(
    #         "//html/body/div/div/div/div[1]/div/div[1]/dl") \
    #         .text_content()
    #
    #     assert "Amount20 EUR" in visa
    #     page3.close()

    @allure.step
    def payment_mastercard_paygate(self):
        """Open new deposit window with mastercard_paygate and try to find element"""
        self.page.locator("li:nth-child(4) > .paymentList__img").click()
        self.page.locator("[placeholder=\"\\30 \"]").fill("20")
        with self.page.expect_popup() as popup_info:
            self.page.locator("button:has-text(\"Einzahlen\")").click()
        page4 = popup_info.value
        mastercard_paygate = page4.locator("//html/body/div/div/div/div[1]/div/div[1]/dl") \
            .text_content()

        assert "Amount20 EUR" in mastercard_paygate
        page4.close()

    @allure.step
    def payment_mastercard_payment_service(self):
        """Open new deposit window with mastercard_payment_service and try to find element"""
        self.page.locator("li:nth-child(6) > .paymentList__img").click()
        self.page.locator("[placeholder=\"\\30 \"]").fill("20")
        with self.page.expect_popup() as popup_info:
            self.page.locator("button:has-text(\"Einzahlen\")").click()
        page5 = popup_info.value
        mastercard_payment_service = page5.locator("//html/body/section[1]/div/div/div/div/div[2]/div/span[1]") \
            .text_content()

        assert "20.0" in mastercard_payment_service
        page5.close()

    @allure.step
    def close(self):
        """End of test"""
        self.context.close()
        self.browser.close()