from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (
        By.ID, "login_link")
    LOGIN_LINK_INVALID = (
        By.ID, "login_link_inc")
    BASKET_LINK = (
        By.CLASS_NAME, "btn-group .btn.btn-default")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (
        By.ID, "login_form")
    REGISTER_FORM = (
        By.ID, "register_form")
    REGISTER_EMAIL = (
        By.ID, "id_registration-email")
    REGISTER_PASSWORD = (
            By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (
        By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


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
    PRODUCTS_IN_BASKET = (
        By.ID, "basket_formset")
    BASKET_EMPTY_TEXT = (
        By.CSS_SELECTOR, "#content_inner>p")


class Links:
    MAIN_URL = "https://selenium1py.pythonanywhere.com/"
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/accounts/login/"
    PRODUCT_URL_ONE = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    PRODUCT_URL_TWO = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
