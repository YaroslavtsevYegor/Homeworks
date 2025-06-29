import time

from selenium.webdriver.common.by import By


def test_login_page(browser):
    """
    The function `test_login_page` navigates to the administration page, locates elements for username,
    password, submit button, and OpenCart link, and includes a delay before completing.
    
    :param browser: The `browser` parameter in the `test_login_page` function is likely an instance of a
    web browser driver, such as Selenium WebDriver, that is used to automate interactions with a web
    browser. It is used to navigate to web pages, interact with elements on the page, and perform
    various actions as
    """
    browser.get(browser.url + "/administration")
    browser.find_element(value="input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.LINK_TEXT, "OpenCart")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
    time.sleep(2)
