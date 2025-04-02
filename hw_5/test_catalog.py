from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    WebDriverWait(browser, 5).until(EC.title_is('Desktops'))


def test_images(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "img-fluid")))


def test_header_text(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "col"), "Desktops"))


def test_compare_button(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'compare-total')))


def test_hidden_sorting(browser):
    browser.get(browser.current_url + "/catalog/desktops")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//*[text() = 'Price (Low > High)']")))
