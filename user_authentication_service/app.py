#!/usr/bin/env python3
""" Flask App"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """Index route"""
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users():
    """Users route"""
    email = request.form.get('email')
    password = request.form.get('password')
    
    try:
      Auth.register_user(email, password)
      return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
      return jsonify({"message": "email already exists"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
