import json
from unittest.mock import Mock

import pytest
from _pytest.capture import CaptureFixture

from eat_it.controllers import AddUserController, AddUserRequest
from eat_it.repositories import UserRepository


@pytest.fixture
def payload() -> dict:
    return {"first_name": "Jan", "last_name": "Kowalski"}


@pytest.fixture
def user_repository() -> UserRepository:
    return Mock(UserRepository)


@pytest.fixture
def controller(user_repository: UserRepository) -> AddUserController:
    return AddUserController(repository=user_repository)


def test_add_user_controller_has_add_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: AddUserController,
) -> None:
    request = AddUserRequest(user=payload)
    controller.add(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_calls_add_in_repository_on_calling_controller(
        controller: AddUserController,
        repository: Mock,
        payload: dict,
) -> None:
    request = AddUserRequest(user=payload)
    controller.add(request)
    assert repository.add.call_count > 0


def test_add_user_request_has_user_attribute(payload: dict) -> None:
    request = AddUserRequest(user=payload)
    assert request.user
