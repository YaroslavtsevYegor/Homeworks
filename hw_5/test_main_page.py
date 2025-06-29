from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    WebDriverWait(browser, 5).until(EC.title_is('Your Store'))
    assert browser.title == 'Your Store'


def test_check_root(browser):
    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu")))
    assert element.is_displayed()


def test_button_search(browser):
    element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-light btn-lg']")))
    assert element.is_displayed()


def test_opencart_logo(browser):
    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'logo')))
    assert element.is_displayed()


def test_before_button(browser):
    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'carousel-banner-0')))
    assert element.is_displayed()
