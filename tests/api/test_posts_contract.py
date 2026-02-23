import pytest
import requests
from qa_automation.models.post_model import PostModel

ENDPOINT = "/posts"


@pytest.mark.api
def test_posts_contract(api_base_url):
    response = requests.get(f"{api_base_url}{ENDPOINT}", timeout=10)
    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list), "Expected a list of posts"

    for post in posts:
        PostModel.model_validate(post)