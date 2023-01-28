import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('link',
                         ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail(reason="expected result")),
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()

    page.check_name_added_product()
    page.check_price_added_product()


@pytest.mark.xfail(reason="expected result")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="expected result")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_text_empty()


if __name__ == "__main__":
    pytest.main()

# pytest -v -s -rpfX --tb=line test_product_page.py
# pytest -v -s -rpfX --tb=line -m "new" test_product_page.py
