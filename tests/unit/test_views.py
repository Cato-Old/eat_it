


from unittest.mock import Mock

import pytest
from flask import Response
from flask.views import MethodView

from eat_it.controllers import GetUserController
from eat_it.views import UserView


@pytest.fixture
def controller() -> Mock:
    return Mock(GetUserController)


@pytest.fixture
def view(controller: GetUserController) -> UserView:
    return UserView(controller=controller)


def test_user_view_returns_501_on_get_method(view: UserView) -> None:
    actual = view.get("1")
    assert actual.status_code == 501


def test_user_view_returns_response_on_get_method(view: UserView) -> None:
    actual = view.get("1")
    assert isinstance(actual, Response)


def test_user_view_is_subclass_method_view(view: UserView) -> None:
    assert isinstance(view, MethodView)


def test_uses_controller_on_get_method(
    view: UserView,
    controller: Mock,
) -> None:
    view.get("1")
    assert controller.get.call_count > 0
