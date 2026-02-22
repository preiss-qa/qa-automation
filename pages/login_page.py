from config import Config


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

    def is_error_message(self) -> bool:
        return "invalid" in self.flash_text()
