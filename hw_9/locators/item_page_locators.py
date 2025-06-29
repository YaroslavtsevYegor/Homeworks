from selenium.webdriver.common.by import By


class ItemPageLocators(object):

    color_dropdown = By.XPATH, "//select[@class='form-control']"
    red_color = By.XPATH, "//option[contains(text(),'Red')]"
    quantity_field = By.ID, "input-quantity"
    add_to_cart_button = By.XPATH, "//button[contains(text(),'Add to Cart')]"
    shopping_cart_button = By.XPATH, "//span[contains(text(),'Shopping Cart')]"
    radio_medium_option = By.XPATH, "//input[@value=6]"
    checkbox3_option = By.XPATH, "//input[@value = 10]"
    checkbox4_option = By.XPATH, "//input[@value = 11]"
    text_option = By.ID, "input-option208"
    select_option = By.ID, "input-option217"
    textarea_option = By.ID, "input-option209"
    file_button_option = By.ID, "button-upload222"
    file_option = By.ID, "input-option222"
    input_file = By.XPATH, "//input[@type='file']"
    date_option = By.ID, "input-option219"
    time_option = By.ID, "input-option221"
    date_time_option = By.ID, "input-option220"
    success_alert = By.XPATH, "//div[contains(text(),'Success')]"
