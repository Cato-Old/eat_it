from flask import Flask, Response

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)
