from pytest import fixture
from playwright.sync_api import sync_playwright
from page_object.login import LoginDeposit
from page_object.registration import RegistrationDeposit
from page_object.login_four_deposit import LoginDepositFourMethod


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def login_deposit_de(get_playwright):
    login = LoginDeposit(get_playwright)
    yield login
    login.close()


@fixture
def registration_deposit_de(get_playwright):
    registration = RegistrationDeposit(get_playwright)
    yield registration
    registration.close()


@fixture
def login_deposit_de_four_methods(get_playwright):
    login_four_methods = LoginDepositFourMethod(get_playwright)
    yield login_four_methods
    login_four_methods.close()
