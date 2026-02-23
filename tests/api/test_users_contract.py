import pytest
import requests
from qa_automation.models.user_model import UserModel

ENDPOINT = "/users"


@pytest.mark.api
def test_users_contract(api_base_url):
    response = requests.get(f"{api_base_url}{ENDPOINT}", timeout=10)
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list), "Expected a list of users"

    for user in users:
        UserModel.model_validate(user)