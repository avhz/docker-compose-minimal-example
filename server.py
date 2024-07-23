## ============================================================================
## IMPORTS
## ============================================================================

import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

## ============================================================================
## APP LISTING
## ============================================================================

app_1, app_2, app_3 = None, None, None

try:
    from app_1.app import app as app_1
except Exception as e:
    print(f"Error importing app_1: {e}")

try:
    from app_2.app import app as app_2
except Exception as e:
    print(f"Error importing app_2: {e}")

try:
    from app_3.app import app as app_3
except Exception as e:
    print(f"Error importing app_3: {e}")

mounts = {
    "/dash1": app_1.server if app_1 is not None else None,
    "/dash2": app_2.server if app_2 is not None else None,
    "/dash3": app_3.server if app_3 is not None else None,
}

## ============================================================================
## SERVER AND HOMEPAGE
## ============================================================================

server = flask.Flask(__name__)
homepage = flask.Flask(__name__)


@homepage.route("/")
def index():
    return "Home Page"


@homepage.errorhandler(404)
def not_found(error):
    return f"<h1>{error}</h1>"


@server.errorhandler(404)
def not_found(error):
    return f"<h1>{error}</h1>"


@homepage.errorhandler(Exception)
def handle_error(e):
    return f"<h1>Error: {str(e)}</h1>", 500


@server.errorhandler(Exception)
def handle_error(e):
    return f"<h1>Error: {str(e)}</h1>", 500


server.wsgi_app = DispatcherMiddleware(app=homepage, mounts=mounts)

## ============================================================================
## MAIN
## ============================================================================

if __name__ == "__main__":
    server.run(debug=True)
