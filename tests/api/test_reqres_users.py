import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_get_user_1_status_and_id(api):
    r = api.get("/users/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1


@pytest.mark.api
@pytest.mark.smoke
def test_get_user_1_has_email(api):
    r = api.get("/users/1")
    assert r.status_code == 200
    assert "@" in r.json()["email"]


@pytest.mark.api
@pytest.mark.regression
def test_create_post_returns_201_and_id(api):
    payload = {"title": "QA", "body": "hello", "userId": 1}
    r = api.post("/posts", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == "QA"
    assert body["userId"] == 1
    assert "id" in body


@pytest.mark.api
@pytest.mark.regression
def test_not_found_returns_404(api):
    r = api.get("/does-not-exist")
    assert r.status_code == 404


@pytest.mark.api
@pytest.mark.regression
def test_response_time_under_2_seconds(api):
    r = api.get("/posts")
    assert r.elapsed.total_seconds() < 2
