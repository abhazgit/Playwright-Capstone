class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.inventory_container = page.locator(".inventory_container")
        self.add_to_cart_backpack_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.remove_from_cart_backpack_button = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.cart_button = page.locator("#shopping_cart_container")
        self.cart_count = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.first_product = page.locator("[data-test='inventory_item_name']:nth-child(1)")
        self.first_product_price = page.locator("[data-test='inventory_item_price']:nth-child(1)")
        self.second_product = page.locator("[data-test='inventory_item_name']:nth-child(2)")
        self.second_product_price = page.locator("[data-test='inventory_item_price']:nth-child(2)")
        self.sort_container = page.locator("[data-test='product-sort-container']")

    def is_displayed(self):
        return self.inventory_container.is_visible()

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack_button.click()

    def go_to_cart(self):
        self.cart_link.click()

    def get_cart_count(self):
        if self.cart_count.count() == 0:
            return 0
        return int(self.cart_count.inner_text())

    def remove_backpack_from_cart(self):
        self.remove_from_cart_backpack_button.click()

    def sort_by(self, criteria):
        self.sort_container.select_option(label=criteria)

    def get_first_product_price(self):
        return float(self.first_product_price.inner_text().replace("$", ""))

    def get_second_product_price(self):
        return float(self.second_product_price.inner_text().replace("$", ""))