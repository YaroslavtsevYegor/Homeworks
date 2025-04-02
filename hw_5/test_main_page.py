from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    WebDriverWait(browser, 5).until(EC.title_is('Your Store'))


def test_check_root(browser):
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu")))


def test_button_search(browser):
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search"]')))


def test_opencart_logo(browser):
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'logo')))


def test_before_button(browser):
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'carousel-banner-0')))
