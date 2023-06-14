from flask import Flask, Response, request, jsonify
from sqlalchemy import create_engine

from eat_it.controllers import AddUserController, AddUserRequest, GetUserController
from eat_it.repositories import UserRepository
from eat_it.views import UserView


class DBFlask(Flask):
    def run(self, *args, **kwargs):
        create_engine("postgresql://user:password@localhost:5432/user_db")


app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    add_user_request = AddUserRequest(user=user)
    controller.add(request=add_user_request)
    return jsonify(user)


@app.put('/users')
def update_user() -> Response:
    user = request.json
    return jsonify(user)


# @app.get('/users/<id>')
# def get_user(id) -> Response:
#     controller = GetUserController()
#     try:
#         controller.get(id=id)
#     except NotImplementedError:
#         pass
#     return Response(status=501)


user_view = UserView.as_view("user_view", controller=GetUserController())
app.add_url_rule("/users/<id>", view_func=user_view)
