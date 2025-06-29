from pages.login_admin import LoginAdmin


def test_login_page_external(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdmin.USERNAME_INPUT)
    browser.find_element(*LoginAdmin.PASSWORD_INPUT)
    browser.find_element(*LoginAdmin.SUBMIT_BUTTON)
    browser.find_element(*LoginAdmin.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdmin.OPENCART_LINK)
