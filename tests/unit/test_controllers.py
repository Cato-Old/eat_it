import json

import pytest
from _pytest.capture import CaptureFixture

from eat_it.controllers import AddUserController, AddUserRequest


@pytest.fixture
def payload() -> dict:
    return {"first_name": "Jan", "last_name": "Kowalski"}


def test_add_user_controller_has_add_method(capsys: CaptureFixture, payload: dict) -> None:
    controller = AddUserController()
    request = AddUserRequest(user=payload)
    controller.add(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_add_user_request_has_user_attribute(payload: dict) -> None:
    request = AddUserRequest(user=payload)
    assert request.user
