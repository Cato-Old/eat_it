from flask import Flask, Response, request, jsonify

from eat_it.controllers import AddUserController, AddUserRequest
from eat_it.repositories import UserRepository

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    repository = UserRepository()
    controller = AddUserController(repository=repository)
    add_user_request = AddUserRequest(user=user)
    controller.add(request=add_user_request)
    return jsonify(user)


@app.put('/users')
def update_user() -> Response:
    user = request.json
    return jsonify(user)

