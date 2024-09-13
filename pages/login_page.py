from dotenv import dotenv_values
from playwright.sync_api import Page


class LoginPage:
    Username = "#user-name"
    Password = "#password"
    Login_button = "#login-button"
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page, login: str, password: str):
        self.page = page
        self.login = login
        self.password = password
        self.load_page()

    def load_page(self):
        self.page.goto(self.URL)

    def authorization(self) -> Page:
        self.page.wait_for_selector(self.Username).type(self.login)
        self.page.wait_for_selector(self.Password).type(self.password)
        self.page.wait_for_selector(self.Login_button).click()
        return self.page
