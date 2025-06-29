import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    """
    The `pytest_addoption` function in Python adds command-line options for specifying the browser and
    URL when running tests with pytest.
    
    :param parser: In the given code snippet, `parser` is an object that is used to add command-line
    options for the pytest framework. The `pytest_addoption` function is a hook provided by pytest that
    allows you to add custom command-line options
    """
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost:80")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromiumService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=FFOptions(), service=FFService())
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
