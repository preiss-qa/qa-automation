import requests


class ApiClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        # Hilft manchmal gegen Anti-Bot / WAF, und ist generell "clean"
        self.session.headers.update({"User-Agent": "qa-automation-philipp/1.0"})

    def get(self, path: str, **kwargs):
        return self.session.get(self.base_url + path, timeout=self.timeout, **kwargs)

    def post(self, path: str, **kwargs):
        return self.session.post(self.base_url + path, timeout=self.timeout, **kwargs)

    def close(self):
        self.session.close()
