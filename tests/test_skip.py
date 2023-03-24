import pytest
from selene.support.shared import browser


@pytest.fixture(params=[pytest.param("browser_size", id="browser_size"),
                        pytest.param("mobile_size", id="mobile_size")],
                scope="session")
def window_size(request):
    if request.param == "browser_size":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com')
    elif request.param == "mobile_size":
        browser.config.window_width = 400
        browser.config.window_height = 780
        browser.open('https://github.com')


@pytest.mark.parametrize("window_size", ["browser_size", "mobile_size"], indirect=True)
def test_github_desktop(window_size):
    if browser.config.window_width == 400 and browser.config.window_height == 780:
        pytest.skip("Run only desktop version")
    browser.element("[class*='sign-in']").click()


@pytest.mark.parametrize("window_size", ["browser_size", "mobile_size"], indirect=True)
def test_github_mobile(window_size):
    if browser.config.window_width == 1920 and browser.config.window_height == 1080:
        pytest.skip("Run only mobile  version")
    browser.element("[class*='Button']").click()
    browser.element("[class*='sign-in']").click()
