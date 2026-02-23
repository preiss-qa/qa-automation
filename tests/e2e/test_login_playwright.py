import pytest
from qa_automation.config import Config
from qa_automation.pages.login_page import LoginPage


@pytest.mark.e2e
@pytest.mark.smoke
def test_login_success(page):
    login = LoginPage(page)
    login.open()
    login.login(Config.USERNAME, Config.PASSWORD)

    assert "secure area" in login.flash_text()


@pytest.mark.e2e
@pytest.mark.regression
def test_login_invalid_credentials(page):
    login = LoginPage(page)
    login.open()
    login.login("wrong_user", "wrong_password")

    assert login.is_invalid_credentials_error()
