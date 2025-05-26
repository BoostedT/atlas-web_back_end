#!/usr/bin/env python3
"""
This module handles secure logging of user data from a MySQL database.
It includes PII field redaction, environment-based database connection,
and secure log formatting using Python's logging system.
"""

import re
import logging
from typing import List
from os import environ
from mysql.connector import connection
from mysql.connector.connection import MySQLConnection

# Fields considered sensitive and to be redacted from logs
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of field names whose values should be redacted.
        redaction: The string to replace sensitive values with.
        message: The original log message string.
        separator: The character that separates key-value pairs.

    Returns:
        A string with specified field values redacted.
    """
    return re.sub(
        rf'({"|".join(fields)})=.*?{separator}',
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message + separator
    )[:-len(separator)]


class RedactingFormatter(logging.Formatter):
    """
    Custom logging formatter that redacts PII fields from log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize formatter with fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting PII field values.

        Args:
            record: A logging.LogRecord object.

        Returns:
            The formatted string with redacted fields.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Configures and returns a logger named 'user_data'
    that redacts PII fields in its output.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Creates and returns a MySQL connection using environment variables.

    Returns:
        A MySQLConnection object.
    """
    return connection.MySQLConnection(
        user=environ.get("PERSONAL_DATA_DB_USERNAME", "root"),
        password=environ.get("PERSONAL_DATA_DB_PASSWORD", ""),
        host=environ.get("PERSONAL_DATA_DB_HOST", "localhost"),
        database=environ["PERSONAL_DATA_DB_NAME"]
    )


def main() -> None:
    """
    Retrieves and logs user data from the database,
    redacting sensitive fields in the output.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    logger = get_logger()
    headers = [column[0] for column in cursor.description]

    for row in cursor:
        message = "; ".join(f"{key}={value}" for key, value in zip(headers, row)) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
