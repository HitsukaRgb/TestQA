import pytest
from dotenv import dotenv_values
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def load_env():
    data = {**dotenv_values(".env")}
    yield data


@pytest.fixture(scope="function", autouse=True)
def get_login(load_env):
    yield load_env["SWAGLABS_LOGIN"]


@pytest.fixture(scope="function", autouse=True)
def get_password(load_env):
    yield load_env["SWAGLABS_PASSWORD"]


@pytest.fixture(scope="function", autouse=True)
def get_login_page(page: Page, get_login, get_password):
    login_page = LoginPage(page, get_login, get_password)
    yield login_page


@pytest.fixture(scope="function", autouse=True)
def get_after_authorization_page(get_login_page):
    page = get_login_page.authorization()
    yield page


@pytest.fixture(scope="function", autouse=True)
def get_git_token(load_env):
    yield load_env["TOKEN"]


@pytest.fixture(scope="function", autouse=True)
def get_repo_name(load_env):
    yield load_env["REPONAME"]


@pytest.fixture(scope="function", autouse=True)
def get_user_name(load_env):
    yield load_env["USERNAME"]
