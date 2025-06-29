import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = browser.current_url
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step("Open url {url}")
    def open(self, url):
        url = self.base_url + url
        self.logger.info("%s: Opening url: %s" % (self.class_name, url))
        self.browser.get(url)

    @allure.step("Get {locator} element")
    def get_element(self, locator: tuple[str, str], timeout):
        self.logger.debug("%s: Checking if element %s is present" % (self.class_name, locator))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Get {locator} elements")
    def get_elements(self, locator: tuple[str, str], timeout):
        self.logger.debug("%s: Checking if elements %s are present" % (self.class_name, locator))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Click on {locator}")
    def click(self, locator: tuple[str, str], timeout):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, locator))
        ActionChains(self.browser).move_to_element(self.get_element(locator, timeout)).pause(0.5).click().perform()

    @allure.step("Click on {locator} and then fill it with {text}")
    def input_value(self, locator: tuple[str, str], text: str, timeout):
        self.logger.debug("%s: Input %s in field %s" % (self.class_name, text, locator))
        self.get_element(locator, timeout).click()
        self.get_element(locator, timeout).clear()
        for l in text:
            self.get_element(locator, timeout).send_keys(l)
