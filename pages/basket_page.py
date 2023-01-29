from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Product is presented, but should not be"

    def should_be_text_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            "Text 'Your basket is empty' is not presented"
