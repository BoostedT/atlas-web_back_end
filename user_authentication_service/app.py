#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, jsonify, request, abort
from auth import Auth
from flask import redirect
from auth import _hash_password

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def index():
    """Index route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """Users route"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already exists"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """Login route"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    """Logout route"""
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
    """Profile route"""
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"])
def reset_password():
    """Reset password"""
    email = request.form.get("email")
    if not email:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except Exception:
        abort(403)
    return jsonify({"email": email, "reset_token": reset_token}), 200


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """Update password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    if not email or not reset_token or not new_password:
        abort(403)
    try:
        user = AUTH._db.find_user_by(email=email, reset_token=reset_token)
        hashed_pwd = _hash_password(new_password)
        AUTH._db.update_user(
            user.id, hashed_password=hashed_pwd.decode(), reset_token=None
        )
    except Exception:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
