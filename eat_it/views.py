from flask import Response
from flask.views import MethodView

from eat_it.controllers import GetUserController


class UserView(MethodView):
    def __init__(self, controller: GetUserController) -> None:
        self._get_user_controller = controller

    def get(self, id: str) -> Response:
        try:
            self._get_user_controller.get(int(id))
        except NotImplementedError:
            pass
        return Response(status=501)
