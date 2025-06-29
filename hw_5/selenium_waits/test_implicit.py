from selenium.webdriver.common.by import By
# from selenium_waits.conftest import browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_root(browser):
    # browser.implicitly_wait(5)
    browser.get("https://automationintesting.online")
    browser.find_element(By.CSS_SELECTOR, "#root")

    WebDriverWait(browser, 4, poll_frequency=0.7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#n1ame")), message="Please enter your name")
