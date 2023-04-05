from dataclasses import dataclass

import pytest

from eat_it.repositories import UserRepository


@dataclass
class AddUserRequest:
    user: dict


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def add(self, request: AddUserRequest) -> None:
        print(request.user)


class GetUserController:
    def get(self, id: int):
        raise NotImplementedError
