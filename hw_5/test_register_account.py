from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_continue_button_click(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
    assert element.is_displayed()


def test_firstname_field(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "firstname")))
    assert element.is_displayed()


def test_lastname_field(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "lastname")))
    assert element.is_displayed()


def test_email_field(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "email")))
    assert element.is_displayed()


def test_password_field(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "password")))
    assert element.is_displayed()
