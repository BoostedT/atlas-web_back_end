#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "session_auth":
    """Session authentication"""
    from api.v1.auth.session_auth import SessionAuth

    auth = SessionAuth()
elif auth_type == "basic_auth":
    """Basic authentication"""
    from api.v1.auth.basic_auth import BasicAuth

    auth = BasicAuth()
elif auth_type == "auth":
    from api.v1.auth.auth import Auth

    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Custom Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Custom Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request() -> None:
    """Before request handler"""
    if auth is None:
        return
    excluded_paths = ["/api/v1/status/",
                      "/api/v1/unauthorized/",
                      "/api/v1/forbidden/",
                      "/api/v1/auth_session/login/"]
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None \
            and auth.session_cookie(request) is None:
        abort(401)
    user = auth.current_user(request)
    if user is None:
        abort(403)
    request.current_user = user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
