from playwright.sync_api import Page


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html/"
    ALL_BUTTON_ADDTOCART = "[class='btn btn_primary btn_small btn_inventory ']"
    SHOPPING_CART_LINK = ".shopping_cart_link"

    def __init__(self, page: Page):
        self.page = page
        self.load_page()

    def load_page(self):
        self.page.goto(self.URL)

    def add_item_to_cart(self):
        self.page.locator(self.ALL_BUTTON_ADDTOCART).all()[0].click()

