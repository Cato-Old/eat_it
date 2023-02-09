import json

import pytest

from eat_it.app import app
from eat_it.app import create_user
from eat_it.app import update_user


@pytest.fixture
def payload() -> dict:
    return {"first_name": "Jan", "last_name": "Kowalski"}


def test_create_user_returns_user(payload: dict) -> None:
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = create_user()
    assert result.json == payload


def test_create_user_prints_user_on_console(payload: dict, capsys) -> None:
    with app.test_request_context(method="POST", path="/users", json=payload):
        create_user()
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_update_user_returns_user(payload: dict) -> None:
    with app.test_request_context(method="PUT", path="/users", json=payload):
        result = update_user()
    assert result.json == payload
