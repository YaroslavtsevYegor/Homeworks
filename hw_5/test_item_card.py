from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_button(browser):
    browser.get(browser.current_url + "/product/desktops/ipod-classic")
    element = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, 'button-cart'), 'Add to Cart'))


def test_brand_button(browser):
    browser.get(browser.current_url + "/product/desktops/ipod-classic")
    element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Apple']")))
    assert element.is_displayed()


def test_review_is_hidden(browser):
    browser.get(browser.current_url + "/product/desktops/ipod-classic")
    element = WebDriverWait(browser, 5).until(EC.invisibility_of_element((By.ID, "form-review")))
    assert element.is_enabled()


def test_like_compare_buttons(browser):
    browser.get(browser.current_url + "/product/desktops/ipod-classic")
    element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-group')))
    assert element.is_displayed()


def test_item_name(browser):
    browser.get(browser.current_url + "/product/desktops/ipod-classic")
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text() = 'iPod Classic']")))
    assert element.is_displayed()
