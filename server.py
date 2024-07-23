import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from app_1.app import app as app_1
from app_2.app import app as app_2


server = flask.Flask(__name__)
home = flask.Flask(__name__)


@home.route("/")
def index():
    return "Home Page"


server.wsgi_app = DispatcherMiddleware(
    app=home,
    mounts={
        "/dash1": app_1.server,
        "/dash2": app_2.server,
    },
)

if __name__ == "__main__":
    server.run(debug=True)
