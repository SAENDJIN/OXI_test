from pytest import fixture
from playwright.sync_api import sync_playwright
from page_object.login import
from page_object.registration import

@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright
