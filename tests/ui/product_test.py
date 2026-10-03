import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestProducts:
    @pytest.fixture(autouse=True)
    def remove_backpack_after_test(self, page):
        yield
        products_page = ProductsPage(page)
        if products_page.remove_from_cart_backpack_button.is_visible():
            products_page.remove_backpack_from_cart()

    @pytest.fixture(autouse=True)
    def sort_to_default(self, page):
        self.sort_products_by(page, "Name (A to Z)")

    @pytest.mark.smoke
    def test_add_backpack_to_cart(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        products_page.add_backpack_to_cart()
        assert products_page.get_cart_count() == 1
        products_page.go_to_cart()

    @pytest.mark.smoke
    def test_remove_backpack_from_cart(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        products_page.add_backpack_to_cart()
        products_page.go_to_cart()
        products_page.remove_backpack_from_cart()
        assert products_page.get_cart_count() == 0

    def sort_products_by(self, page, criteria):
        criteria = "Name (A to Z)";
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        products_page = ProductsPage(page)
        products_page.sort_by(criteria)
        assert products_page.is_displayed()
