import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import Links


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, Links.MAIN_URL)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, Links.MAIN_URL)
        page.open()
        page.should_be_login_link()


def test_guest_should_see_login_page(browser):
    page = LoginPage(browser, Links.LOGIN_URL)
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, Links.MAIN_URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_text_empty()


if __name__ == "__main__":
    pytest.main()

# pytest -v -rpf --tb=line test_main_page.py
# pytest -v -rpf --tb=line -m "login_guest" test_main_page.py
