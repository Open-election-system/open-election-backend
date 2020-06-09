from flask import Flask
import werkzeug
from app import application


def format_exception(error, error_code):
    application.logger.error(str(error) + " " + str(error_code))
    return {
        "error": {
            "code": error_code,
            "message": error
        }
    }, error_code


class CustomException(werkzeug.exceptions.HTTPException):
    code = int


class CustomNotFound(CustomException, werkzeug.exceptions.NotFound):
    code = 404


class CustomInternalServerError(CustomException, werkzeug.exceptions.InternalServerError):
    code = 500


class CustomUnauthorized(CustomException, werkzeug.exceptions.UnprocessableEntity):
    code = 401

class EmailInUseException(CustomUnauthorized):
    description = "This email address is already being used"

class IncorectCredentials(CustomUnauthorized):
    description = "The email address or password is incorect "