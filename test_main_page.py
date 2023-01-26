from selenium.webdriver.common.by import By
import pytest


link = 'https://selenium1py.pythonanywhere.com/'


def go_to_login_page(browser):
    login_link = browser.find_element(
        By.CSS_SELECTOR, "#login_link"
    )
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)


if __name__ == "__main__":
    pytest.main()

# https://stepik.org/lesson/199980/step/6?auth=login&next=&unit=174035

# pytest -v --tb=line --language=en test_main_page.py
