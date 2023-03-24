import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com')


def test_github_desktop(browser_size):
    browser.element("[class*='sign-in']").click()


@pytest.fixture()
def mobile_size():
    browser.config.window_width = 400
    browser.config.window_height = 780
    browser.open('https://github.com')


def test_github_mobile(mobile_size):
    browser.element("[class*='Button']").click()
    browser.element("[class*='sign-in']").click()