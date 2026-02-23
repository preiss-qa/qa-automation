from qa_automation.config import Config


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.submit = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")

    def open(self):
        self.page.goto(Config.LOGIN_URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()

    def flash_text(self) -> str:
        return self.flash.inner_text().lower()

    def is_invalid_credentials_error(self) -> bool:
        text = self.flash_text()
        return ("your username is invalid" in text) or ("your password is invalid" in text)