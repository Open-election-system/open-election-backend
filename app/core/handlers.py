from flask import Flask

from app import application
from app.core.exceptions import(
    format_exception,
    EmailInUseException,
)

# Base exceptions handlers

@application.errorhandler(IndexError)
@application.errorhandler(ValueError)
@application.errorhandler(FileExistsError)
@application.errorhandler(RuntimeError)
@application.errorhandler(TypeError)
@application.errorhandler(AttributeError)
@application.errorhandler(NameError)
def base_exceptions_handler(error):
    return format_exception(str(*error.args), 500)

@application.errorhandler(FileNotFoundError)
def file_not_found_handler(error):
    return format_exception(str(*error.args), 404) 

# Custom exceptions handler

@application.errorhandler(Exception)
def custom_exceptions_error_handler(error):
    if isinstance(error, CustomException):
        print(error)
        return format_exception(error.description, error.code)


