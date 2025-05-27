#!/usr/bin/env python3
"""Session Authentication that inherits from Auth"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """SessionAuth class that handles Session Authentication"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user_id.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str) -> str:
        """
        Retrieves the user ID associated with a session ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    def extract_session_id_from_request(self, request) -> str:
        """
        Extracts the session ID from the request cookies.
        """
        if request is None or not hasattr(request, "cookies"):
            return None

        return request.cookies.get("session_id")

    def current_user(self, request=None) -> str:
        """
        Retrieves the current user based on the session ID in the request.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Destroys the session for the current user.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del SessionAuth.user_id_by_session_id[session_id]
        return True
