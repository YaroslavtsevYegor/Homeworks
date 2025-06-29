import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromiumService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=FFOptions(), service=FFService())
    else:
        driver = webdriver.Safari()
    driver.maximize_window()
    request.addfinalizer(driver.close)

    # driver.implicitly_wait(3)

    return driver
