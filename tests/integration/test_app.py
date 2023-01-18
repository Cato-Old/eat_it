from eat_it.app import app

UNIMPLEMENTED = 501


def test_app_has_ping_endpoint() -> None:
    client = app.test_client()
    response = client.get(path="/ping")
    assert response.status_code == UNIMPLEMENTED


def test_app_user_create_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == 200
