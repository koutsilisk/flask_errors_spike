from werkzeug.exceptions import HTTPException


class LoginError(Exception):
    status_code: int = 400
    insternal_code: str = "LOGIN_ERROR"
    message: str = "Error at login"

    def __init__(self, message: str = None, *args: object) -> None:
        super().__init__(*args)
        if message is not None:
            self.message = message


class InvalidCredentialsError(LoginError):
    status_code: int = 401
    insternal_code: str = "INVALID_CREDENTIALS"
    message: str = "Invalid credentials provided, please try again"

    def __init__(self, message: str = None, *args: object) -> None:
        super().__init__(*args)
        if message is not None:
            self.message = message

    def to_dict(self) -> dict:
        error: dict = {
            "code": self.insternal_code,
            "message": self.message,
        }
        return error


class InvalidParameter(LoginError):
    status_code: int = 400
    insternal_code: str = "INVALID_PARAMETER"
    message: str = "Invalid parameter provided"

    def __init__(
        self,
        message: str = None,
        parameter: str = None,
        value: object = None,
        *args: object
    ) -> None:
        super().__init__(*args)
        if message is not None:
            self.message = message
        self.parameter = parameter
        self.value = value

    def to_dict(self) -> dict:
        error: dict = {
            "code": self.insternal_code,
            "message": self.message,
        }
        if self.parameter:
            error["parameter"] = self.parameter
        if self.value:
            error["value"] = self.value
        return error


class DeactivatedUserError(LoginError):
    status_code: int = 403
    insternal_code: str = "USER_DEACTIVATED"
    message: str = (
        "User accound is not active, please contact administration to fix this issue"
    )

    def __init__(self, message: str = None, *args: object) -> None:
        super().__init__(*args)
        if message is not None:
            self.message = message

    def to_dict(self) -> dict:
        error: dict = {
            "code": self.insternal_code,
            "message": self.message,
        }
        return error
