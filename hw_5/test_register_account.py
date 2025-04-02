from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_continue_button_click(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))


def test_firstname_field(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "firstname")))


def test_lastname_field(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "lastname")))


def test_email_field(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "email")))


def test_password_field(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "password")))
