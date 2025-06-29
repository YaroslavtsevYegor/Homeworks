from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hw_9.pages.base_page import BasePage
from hw_9.locators.item_page_locators import ItemPageLocators
import allure
import os
from dotenv import load_dotenv
load_dotenv()
filepath = os.getenv("file_path")


class ItemPage(BasePage):

    @allure.step("Выбрать {color} цвет для товара")
    def select_color(self, color='Red', timeout=5):
        self.logger.info("%s: Выбор цвета товара %s" % (self.class_name, color))
        self.get_element(ItemPageLocators.color_dropdown, timeout)
        self.select_from_dropdown(
            ItemPageLocators.color_dropdown, color, timeout)

    @allure.step("Ввести {qty} в количество товара")
    def fill_in_quantity(self, qty='2', timeout=5):
        self.logger.info("%s: Ввод %s в количество товара" %
                         (self.class_name, qty))
        self.get_element(ItemPageLocators.quantity_field, timeout)
        self.input_value(ItemPageLocators.quantity_field, qty, timeout)

    @allure.step("Добавить продукт в корзину")
    def add_to_cart(self, timeout=5):
        self.logger.info("%s: Добавление товара в корзину" % (self.class_name))
        self.get_element(ItemPageLocators.add_to_cart_button, timeout)
        self.click(ItemPageLocators.add_to_cart_button, timeout)

    @allure.step("Выбрать доступные опции для товара")
    def choose_available_options(self, text='Текст', select="Yellow", date='2020-09-20', time='16:05', qty='2', timeout=5):
        self.logger.info("%s: Заполнение опций на странице товара" % (self.class_name))
        self.get_element(ItemPageLocators.radio_medium_option, timeout)
        self.click(ItemPageLocators.radio_medium_option, timeout)
        self.get_element(ItemPageLocators.checkbox3_option, timeout)
        self.click(ItemPageLocators.checkbox3_option, timeout)
        self.get_element(ItemPageLocators.checkbox4_option, timeout)
        self.click(ItemPageLocators.checkbox4_option, timeout)
        self.get_element(ItemPageLocators.text_option, timeout)
        self.input_value(ItemPageLocators.text_option, text, timeout)
        self.get_element(
            ItemPageLocators.select_option, timeout)
        self.select_from_dropdown(
            ItemPageLocators.select_option, select, timeout)
        self.get_element(ItemPageLocators.textarea_option, timeout)
        self.input_value(ItemPageLocators.textarea_option, text, timeout)
        self.upload_new_file(
            ItemPageLocators.file_button_option, ItemPageLocators.input_file, filepath, timeout)
        WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        alert.accept()
        self.get_element(ItemPageLocators.date_option, timeout)
        self.input_value(ItemPageLocators.date_option, date, timeout)
        self.get_element(ItemPageLocators.time_option, timeout)
        self.input_value(ItemPageLocators.time_option, time, timeout)
        self.get_element(ItemPageLocators.date_time_option, timeout)
        self.input_value(ItemPageLocators.date_time_option,
                         date+' '+time, timeout)
        self.get_element(ItemPageLocators.quantity_field,  timeout)
        self.input_value(ItemPageLocators.quantity_field, qty, timeout)
        self.get_element(ItemPageLocators.add_to_cart_button, timeout)
        self.click(ItemPageLocators.add_to_cart_button, timeout)
        self.get_element(ItemPageLocators.success_alert, timeout)
