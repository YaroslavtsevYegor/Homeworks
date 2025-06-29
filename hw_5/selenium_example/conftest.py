import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")
    # driver = None
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
            # options.add_argument("headless=new")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError("Browser name must be either 'chrome', 'firefox' or 'edge'")

    if maximize:
        driver.maximize_window()

    yield driver
    driver.quit()
