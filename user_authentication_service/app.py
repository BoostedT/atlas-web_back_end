#!/usr/bin/env python3
""" Flask App"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Index route"""
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users():
    """Users route"""
    email = request.forms.get('email')
    password = request.forms.get('password')
    
    try:
      user = Auth.register_user(email, password)
      return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
      return jsonify({"message": "email already exists"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
