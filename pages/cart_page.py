from playwright.sync_api import Page


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"
    CART_ITEM = ".cart_item"
    CHECKOUT = "#checkout"

    def __init__(self, page: Page):
        self.page = page
        self.load_page()
        self.count_card_item = self.page.locator(self.CART_ITEM).count()

    def load_page(self):
        self.page.goto(self.URL)

    def checkout(self) -> Page:
        self.page.locator(self.CHECKOUT).click()
        return self.page
