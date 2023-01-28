import pytest
from .pages.product_page import ProductPage


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
                              marks=pytest.mark.xfail),
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()

    page.check_name_added_product()
    page.check_price_added_product()


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.xfail(reason="expected result")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="expected result")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_success_message_disappear()


if __name__ == "__main__":
    pytest.main()

# pytest -v -s -rpfxX --tb=line --language=en test_product_page.py
