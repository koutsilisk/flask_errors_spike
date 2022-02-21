from flask import Flask, jsonify, request
from errors import (
    LoginError,
    InvalidCredentialsError,
    InvalidParameter,
    DeactivatedUserError,
)

app = Flask(__name__)


@app.errorhandler(LoginError)
def invald_credentials_handler(e):
    return jsonify(errors=[e.to_dict()]), e.status_code


@app.route("/", methods=["GET"])
def index():
    return jsonify(message="hello errors")


@app.route("/login", methods=["POST"])
def login():
    user: dict = dict(id=1, username="test", email="test@test.test")
    username: str = request.json.get("username")
    password: str = request.json.get("password")

    active: bool = True  # set to False in order to deactivate user

    if username is None:
        raise InvalidParameter(
            message="Please provide a username",
            parameter="username",
            value="Not provided",
        )
    elif password is None:
        raise InvalidParameter(
            message="Please provide a password",
            parameter="password",
            value="Not provided",
        )
    elif not active:
        raise DeactivatedUserError()
    elif username == "test" and password == "test123":
        return jsonify(user)
    else:
        raise InvalidCredentialsError()


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
