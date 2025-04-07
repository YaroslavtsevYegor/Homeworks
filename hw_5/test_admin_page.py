from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_button_click(browser):
    browser.get(browser.current_url + "/administration")
    element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
    assert element.is_displayed()


def test_username_field(browser):
    browser.get(browser.current_url + "/administration")
    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "input-username")))
    assert element.is_displayed()


def test_password_field(browser):
    browser.get(browser.current_url + "/administration")
    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "input-password")))
    assert element.is_displayed()


def test_login_button_visible(browser):
    browser.get(browser.current_url + "/administration")
    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
    assert element.is_displayed()


def test_admin_title(browser):
    browser.get(browser.current_url + "/administration")
    element = WebDriverWait(browser, 5).until(EC.title_is('Administration'))
    assert browser.title == 'Administration'
