from functools import wraps

from peewee import SqliteDatabase

from .error_code import error


def use_database(db_instance):
    """
    this decorator is used for opening and closing connection to the database
    """

    def decorator(function):
        @wraps(function)
        def connection_handler(*args, **kwargs):
            if not isinstance(db_instance, SqliteDatabase):
                return error(1013)

            if not before_request_handler(db_instance):
                return error(1003)

            try:
                response = function(*args, **kwargs)
                return response
            finally:
                after_request_handler(db_instance)

        return connection_handler

    return decorator


def before_request_handler(db_instance):
    try:
        if not db_instance.is_closed():
            return True
        db_instance.connect()
        return True
    except Exception as e:
        return False


def after_request_handler(db_instance):
    if not db_instance.is_closed():
        db_instance.close()
