import pytest
from qa_automation.config import Config
from utils.api.client import ApiClient
from playwright.sync_api import sync_playwright


# ---------- API fixtures ----------

@pytest.fixture(scope="session")
def api_base_url():
    return Config.BASE_API_URL


@pytest.fixture()
def api(api_base_url):
    client = ApiClient(base_url=api_base_url, timeout=10)
    yield client
    client.close()


# ---------- E2E fixtures ----------

@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p


@pytest.fixture()
def page(pw):
    browser = pw.chromium.launch(headless=Config.HEADLESS)
    page = browser.new_page()
    yield page
    browser.close()
