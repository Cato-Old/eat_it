from dataclasses import dataclass


@dataclass
class AddUserRequest:
    user: dict


class AddUserController:
    def add(self, request: AddUserRequest) -> None:
        print(request.user)
