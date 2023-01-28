from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (
        By.ID, "login_link")
    LOGIN_LINK_INVALID = (
        By.ID, "login_link_inc")
    BASKET_LINK = (
        By.CLASS_NAME, "btn-group .btn.btn-default")


class MainPageLocators:
    pass


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


class BasketPageLocators:
    PRODUCT_PRICE_BASKET = (
        By.CLASS_NAME, "price_color.align-right")
    PRODUCT_IMG_BASKET = (
            By.CLASS_NAME, "thumbnail")
    BASKET_EMPTY_TEXT = (
        By.CSS_SELECTOR, "#content_inner>p")
