import pytest
import requests
from qa_automation.models.user_model import UserModel

ENDPOINT = "/users"
USER_ID = 1


@pytest.mark.api
def test_user_by_id_contract(api_base_url):
    response = requests.get(f"{api_base_url}{ENDPOINT}/{USER_ID}", timeout=10)
    assert response.status_code == 200

    user = response.json()
    assert isinstance(user, dict), "Expected a single user object (dict)"

    UserModel.model_validate(user)