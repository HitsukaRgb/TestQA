from playwright.sync_api import Page


class CheckoutPage:
    URL_STEP_ONE = "https://www.saucedemo.com/checkout-step-one.html"
    URL_STEP_TWO = "https://www.saucedemo.com/checkout-step-two.html"
    URL_CHECKOUT_COMPLETE = "https://www.saucedemo.com/checkout-complete.html"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = "#continue"
    CART_ITEM = ".cart_item"
    FINISH = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def __init__(self, page: Page):
        self.page = page
        self.load_page()

    def load_page(self):
        self.page.goto(self.URL_STEP_ONE)

    def press_continue_button(self) -> Page:
        self.page.wait_for_selector(self.CONTINUE).click()
        return self.page

    def press_finish_button(self) -> Page:
        self.page.locator(self.FINISH).click()
        return self.page

    def fill_first_name(self, value: str):
        self.page.wait_for_selector(self.FIRST_NAME).type(value)

    def fill_last_name(self, value: str):
        self.page.wait_for_selector(self.LAST_NAME).type(value)

    def fill_postal_code(self, value: str):
        self.page.wait_for_selector(self.POSTAL_CODE).type(value)

    @property
    def get_complete_header(self):
        if self.page.url == self.URL_CHECKOUT_COMPLETE:
            return self.page.locator(self.COMPLETE_HEADER).text_content()
        return None
