from eat_it.app import ping, create_user, app

UNIMPLEMENTED = 501


def test_ping_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED


def test_create_user_returns_user() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = create_user()
    assert result.json == payload
