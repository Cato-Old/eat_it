import pytest

from eat_it.repositories import UserRepository


@pytest.fixture
def repository() -> UserRepository:
    return UserRepository()


def test_can_instantiate_user_repository(
    repository: UserRepository,
) -> None:
    pass


def test_raises_on_add_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.add()
