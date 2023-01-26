import pytest
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


if __name__ == "__main__":
    pytest.main()

# pytest -v --tb=line --language=en test_main_page.py
