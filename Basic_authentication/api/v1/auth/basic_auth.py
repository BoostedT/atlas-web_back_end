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

        return authorization_header[len("Basic ") : ]
