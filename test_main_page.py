import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


if __name__ == "__main__":
    pytest.main()

# pytest -v -rpf --tb=line --language=en test_main_page.py
