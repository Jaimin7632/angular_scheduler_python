import flask
from flask import request

from database_utils import utils as db_utils

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/backend_create.php', methods=['GET'])
def backend_create():
    return db_utils.create_events(**request.args)


@app.route('/api/backend_events.php', methods=['GET'])
def backend_events():
    return db_utils.get_backend_events(**request.args)


@app.route('/api/backend_move.php', methods=['GET'])
def backend_move():
    return db_utils.update_backend_move(**request.args)


@app.route('/api/backend_resources.php', methods=['GET'])
def backend_create():
    return db_utils.get_backend_resources()


if __name__ == "__main__":
    app.run()
    # print(db_utils.get_backend_resources())
    # print(db_utils.backend_create(name='cvt', start=datetime.now(), end=datetime.now(), resource='1'))
    # print(db_utils.get_backend_events(frm=datetime.now(), to=datetime.now()))
