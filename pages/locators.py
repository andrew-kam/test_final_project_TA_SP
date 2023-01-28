from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (
        By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (
        By.ID, "login_form")
    REGISTER_FORM = (
        By.ID, "register_form")


class ProductPageLocators:
    BASKET_LINK = (
        By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (
        By.CLASS_NAME, "product_main h1")
    PRODUCT_PRICE = (
        By.CLASS_NAME, "product_main .price_color")
    PRODUCT_NAME_ADDED = (
        By.CLASS_NAME, "alert-success strong")
    PRODUCT_PRICE_ADDED = (
        By.CLASS_NAME, "alert-info strong")
    SUCCESS_MESSAGE = (
        By.CLASS_NAME, "alert-success")
