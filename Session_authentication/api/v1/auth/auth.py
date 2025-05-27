#!/usr/bin/env python3
"""Auth class for managing API authentication"""

from flask import request
from typing import List, TypeVar
from os import getenv

class Auth:
    """Template for all authentication systems"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.

        Args:
            path (str): The request path.
            excluded_paths (List[str]): Paths that do not require auth.

        Returns:
            bool: True if auth is required, False if the path is excluded.
        """
        if path is None or not excluded_paths:
            return True

        if not path.endswith("/"):
            path += "/"

        for excluded in excluded_paths:
            if excluded == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header from the request.

        Args:
            request: Flask request object.

        Returns:
            str: None for now.
        """
        if request is None:
            return None

        auth_header = request.headers.get("Authorization")
        if auth_header is None:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Returns the current user.
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns the session cookie from the request."""
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        if not session_name:
            return None

        return request.cookies.get("session_id")
