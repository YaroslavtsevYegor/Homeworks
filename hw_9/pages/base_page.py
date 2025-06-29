import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import pyautogui


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = browser.current_url
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step("Открыть страницу {url}")
    def open(self, url=''):
        url = self.base_url + url
        self.logger.info("%s: Переход на страницу: %s" % (self.class_name, url))
        self.browser.get(url)

    @allure.step("Перезагрузка страницы")
    def refresh_page(self, timeout = 5):
        self.logger.info("%s: Обновление страницы" % (self.class_name))
        self.browser.refresh()
        WebDriverWait(self.browser, timeout).until(
            lambda browser: browser.execute_script(
                "return document.readyState") == "complete"
        )

    @allure.step("Найти элемент {locator}")
    def get_element(self, locator: tuple[str, str], timeout=5):
        self.logger.debug("%s: Проверка наличия элемента %s на странице" %
                          (self.class_name, locator))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элементы {locator}")
    def get_elements(self, locator: tuple[str, str], timeout=5):
        self.logger.debug("%s: Проверка наличия элементов %s на странице" %
                          (self.class_name, locator))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Нажать на {locator}")
    def click(self, locator: tuple[str, str], timeout=5):
        self.logger.debug("%s: Нажатие на элемент: %s" %
                          (self.class_name, locator))
        ActionChains(self.browser).move_to_element(
            self.get_element(locator, timeout)).pause(0.5).click().perform()

    @allure.step("Нажать на {locator} и ввести {text}")
    def input_value(self, locator: tuple[str, str], text: str, timeout=5):
        self.logger.debug("%s: Ввод текста %s в поле %s" %
                          (self.class_name, text, locator))
        self.get_element(locator, timeout).click()
        self.get_element(locator, timeout).clear()
        for l in text:
            self.get_element(locator, timeout).send_keys(l)

    @allure.step("Нажать на {locator} и выбрать {text}")
    def select_from_dropdown(self, locator: tuple[str, str], text: str, timeout=5):
        self.logger.debug("%s: Нажатие на элемент %s и выбор опции %s" % (
            self.class_name, locator, text))
        select = Select(self.get_element(locator, timeout))
        for option in select.options:
            if text in option.text:
                option.click()
                break

    @allure.step('Загрузить файл')
    def upload_new_file(self, button_locator, fileinput_locator, filepath, timeout=5):
        self.logger.debug("%s: Нажатие на элемент %s и загрузка файла %s" % (
            self.class_name, button_locator, filepath))
        self.click(button_locator, timeout)
        if not self.browser.is_headless:
            try:
                time.sleep(1)
                pyautogui.press('esc')
            except Exception:
                print('Не работает')
        file_input = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(fileinput_locator))
        file_input.send_keys(filepath)
