import pytest

from pages.login_page import LoginPage

import json
from pathlib import Path

LOGIN_DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "login_data.json"
LOGIN_DATA = json.loads(LOGIN_DATA_PATH.read_text())

class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.parametrize("login_data", LOGIN_DATA)

    def test_login(self, page, login_data):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(login_data["username"], login_data["password"])
        assert page.url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.smoke
    def test_login_invalid(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "invalid_pass")
        assert page.url == "https://www.saucedemo.com/"

