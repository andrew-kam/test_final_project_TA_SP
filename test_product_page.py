import pytest
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()

    page.check_name_added_product()
    page.check_price_added_product()


if __name__ == "__main__":
    pytest.main()

# pytest -v -s -rpf --tb=line --language=en test_product_page.py
