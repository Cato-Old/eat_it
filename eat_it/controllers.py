from dataclasses import dataclass

from eat_it.repositories import UserRepository


@dataclass
class AddUserRequest:
    user: dict


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        pass

    def add(self, request: AddUserRequest) -> None:
        print(request.user)
