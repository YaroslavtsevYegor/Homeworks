from selenium.webdriver.common.by import By


class ComparisonPageLocators(object):

    remove_from_comparison_button = By.XPATH, "//a[contains(text(),'Remove')]"
    add_to_cart_from_comparison_button = By.XPATH, "//input[@value='Add to Cart']"
