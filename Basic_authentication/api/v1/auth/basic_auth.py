#!/usr/bin/env python3
"""
Basic authentication module for API v1
"""

from api.v1.auth.auth import Auth


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

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_pass = decoded_base64_authorization_header.split(':', 1)
        if len(user_pass) != 2:
            return None, None

        return user_pass[0], user_pass[1]
