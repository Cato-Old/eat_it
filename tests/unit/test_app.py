


from unittest.mock import patch, call

import pytest
from flask import Flask

from eat_it.app import DBFlask


@pytest.fixture
def db_flask() -> DBFlask:
    return DBFlask("dummy_import_name")


def test_db_flask_is_subclass_of_flask(db_flask: DBFlask) -> None:
    assert isinstance(db_flask, Flask)


def test_raises_on_run_method(db_flask: DBFlask) -> None:
    expected = call(  )
    with patch("eat_it.app.create_engine") as mock:
        db_flask.run()
    assert expected in mock.mock_calls
