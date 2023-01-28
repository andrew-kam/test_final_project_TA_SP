from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_to_basket(self):
        basket_link = self.browser.find_element(
            *ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def check_name_added_product(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        product_name_added = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ADDED)
        assert product_name.text == product_name_added.text,\
            "Product name in basket isn`t correct"

    def check_price_added_product(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        product_price_added = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_ADDED)
        assert product_price.text == product_price_added.text,\
            "Product price in basket isn`t correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"
