#!/usr/bin/env python3
"""Session Authentication that inherits from Auth"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth class that handles Session Authentication"""

    def extract_session_id_from_request(self, request) -> str:
        """
        Extracts the session ID from the request.

        Args:
            request: The request object.

        Returns:
            str or None: The session ID, or None if not found.
        """
        if request is None or not hasattr(request, "cookies"):
            return None

        return request.cookies.get("session_id", None)
