from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = browser.current_url

    def open(self, url):
        url = self.base_url + url
        self.browser.get(url)

    def get_title(self):
        return self.browser.title

    def get_url(self):
        return self.browser.current_url

    def get_element(self, locator: tuple[str, str], timeout):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple[str, str], timeout):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple[str, str], timeout):
        ActionChains(self.browser).move_to_element(self.get_element(locator, timeout)).pause(0.5).click().perform()

    def input_value(self, locator: tuple[str, str], text: str, timeout):
        self.get_element(locator, timeout).click()
        self.get_element(locator, timeout).clear()
        for l in text:
            self.get_element(locator, timeout).send_keys(l)
