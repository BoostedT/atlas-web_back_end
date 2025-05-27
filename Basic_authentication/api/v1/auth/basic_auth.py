#!/usr/bin/env python3
"""
Basic authentication module for API v1
"""

from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class that handles Basic Authentication"""

    def extract_base64_authorization_header(
      self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Auth.

        Args:
            authorization_header (str): The full Authorization header.

        Returns:
            str or None: The Base64 part of the header, or None if invalid.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 part of the Authorization header.

        Args:
            base64_authorization_header (str): The Base64 encoded string.

        Returns:
            str or None: The decoded string, or None if invalid.
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        import base64

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts user credentials from the decoded Base64 Authorization header.

        Args:
            decoded_base64_authorization_header (str): The decoded string.

        Returns:
            tuple: A tuple containing the username and password,
            or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None

        user_pass = decoded_base64_authorization_header.split(":", 1)
        if len(user_pass) != 2:
            return None, None

        return user_pass[0], user_pass[1]

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """
        Retrieves a user object based on email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User or None: The user object if found,
            or None if not found.
        """
        if user_email is None or user_pwd is None:
            return None

        from models.user import User

        try:
            user = User.search({"email": user_email})
            if not user:
                return None
            for u in user:
                if u.is_valid_password(user_pwd):
                    return u
        except Exception:
            return None

        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieves the current user from the request.

        Args:
            request: The request object.

        Returns:
            User or None: The current user object if found,
            or None if not found.
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_auth)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
