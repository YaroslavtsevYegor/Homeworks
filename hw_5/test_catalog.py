from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    element = WebDriverWait(browser, 5).until(EC.title_is('Desktops'))
    assert browser.title == 'Desktops'


def test_images(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "img-fluid")))
    assert element.is_displayed()


def test_header_text(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "col"), "Desktops"))


def test_compare_button(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'compare-total')))
    assert element.is_displayed()


def test_hidden_sorting(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//option[text() = 'Price (Low > High)']")))
    assert element.is_displayed()
