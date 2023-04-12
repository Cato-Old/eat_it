



import pytest
from flask import Response
from flask.views import MethodView

from eat_it.views import UserView


@pytest.fixture
def view() -> UserView:
    return UserView()


def test_user_view_returns_501_on_get_method(view: UserView) -> None:
    actual = view.get("1")
    assert actual.status_code == 501


def test_user_view_returns_response_on_get_method(view: UserView) -> None:
    actual = view.get("1")
    assert isinstance(actual, Response)


def test_user_view_is_subclass_method_view(view: UserView) -> None:
    assert isinstance(view, MethodView)
