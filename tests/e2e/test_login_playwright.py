import pytest

URL = "https://the-internet.herokuapp.com/login"
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


@pytest.mark.e2e
@pytest.mark.smoke
def test_login_success(page):
    page.goto(URL)
    page.locator("#username").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("button[type='submit']").click()

    assert "secure area" in page.locator("#flash").inner_text().lower()
