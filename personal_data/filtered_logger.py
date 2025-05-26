#!/usr/bin/env python3
"""Filtered logger module"""
import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Redacts specified fields in a log message."""
    return re.sub(
        rf'({"|".join(fields)})=.*?{separator}',
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message + separator,
    )[: -len(separator)]


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats a log record, redacting specified fields."""
        original = super().format(record)
        return filter_datum(
          self.fields, self.REDACTION, original, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates and returns a logger named 'user_data'
    with custom redacting formatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Returns a MySQL connector
    connection using credentials
    from environment variables.
    """
    return mysql.connector.connect(
        user=os.environ.get("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.environ.get("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.environ.get("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.environ["PERSONAL_DATA_DB_NAME"]
    )
