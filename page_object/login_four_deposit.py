from playwright.sync_api import Playwright, sync_playwright, expect
import allure


class LoginDepositFourMethod:
    """
    Test user flow login ->
    deposit (bank_uberweisung_black / bank_uberweisung_white / visa / mastercard_paygate / mastercard_payment_service)
    """

    @allure.step
    def __init__(self, playwright: Playwright):
        """Configure browser to start autotest"""
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://oxicasino.io/")

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
