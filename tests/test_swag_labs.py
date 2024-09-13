from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def test_saucedemo_authorization(get_after_authorization_page):
    """Проверка авторизации"""
    assert get_after_authorization_page.url == "https://www.saucedemo.com/inventory.html"


def test_inventory(get_after_authorization_page):
    """Проверка оформления покупки"""
    inventory_page = InventoryPage(get_after_authorization_page)
    inventory_page.page.locator(inventory_page.add_item_to_cart())
    inventory_page.page.locator(inventory_page.SHOPPING_CART_LINK).click()
    cart_page = CartPage(inventory_page.page)
    assert cart_page.count_card_item != 0
    checkout_page = CheckoutPage(cart_page.checkout())
    assert checkout_page.page.url == checkout_page.URL_STEP_ONE
    checkout_page.fill_last_name("LastNameTestQA")
    checkout_page.fill_first_name("FirstNameTestQA")
    checkout_page.fill_postal_code("1234")
    checkout_page.press_continue_button()
    assert checkout_page.page.url == checkout_page.URL_STEP_TWO
    assert checkout_page.page.locator(checkout_page.CART_ITEM).all() != 0
    checkout_page.press_finish_button()
    assert checkout_page.get_complete_header == "Thank you for your order!"




