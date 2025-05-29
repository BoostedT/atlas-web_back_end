#!/usr/bin/env python3
"""authentication"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt and return bytes."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a unique identifier for the user."""
    import uuid

    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with email and password."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)  # ✅ No 'self.'
            return self._db.add_user(email, hashed_password.decode("utf-8"))

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode("utf-8"), user.hashed_password.encode("utf-8")
            )
        except (NoResultFound, Exception):
            return False

    def create_session(self, email: str) -> str:
        """
        Create a session for the user and return the session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """Retrieve a user by their session ID."""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """
        Destroy the session for the user.
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None
          
    def get_reset_password_token(self, email: str) -> str:
      """Generate a reset password token for the user."""
      try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
      except NoResultFound:
            raise ValueError("No user found with this email")