from dataclasses import dataclass

import pytest

from eat_it.repositories import UserRepository


@dataclass
class AddUserRequest:
    user: dict


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def add(self, request: AddUserRequest) -> None:
        self._repository.add()


class GetUserController:
    def get(self, id: int):
        raise NotImplementedError
