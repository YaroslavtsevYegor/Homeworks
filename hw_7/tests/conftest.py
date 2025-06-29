from datetime import datetime
import allure
import pytest
from selenium import webdriver
import logging


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.0.89")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--remote", action="store_true")
    parser.addoption("--headless", action="store_true")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs['browser']
        allure.attach(body=driver.get_screenshot_as_png(), name=item.name + "_failure_screenshot.png",
                      attachment_type=allure.attachment_type.PNG)


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    is_remote = request.config.getoption("--remote")
    is_headless = request.config.getoption("--headless")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler("logs.log", mode='w', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.now()))

    capabilities = {
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True,
        }
    }
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
    if is_headless:
        options.add_argument("--headless")
    if is_remote:
        for k, v in capabilities.items():
            options.set_capability(k, v)
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            options=options
        )
    else:
        if browser_name == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(options=options)
        elif browser_name == "edge":
            driver = webdriver.Edge(options=options)
    driver.log_level = log_level
    driver.logger = logger
    driver.maximize_window()
    driver.get(url)
    logger.info("Browser %s started" % browser_name)
    yield driver
    logger.info("===> Test %s finished at %s" % (request.node.name, datetime.now()))
    driver.quit()
