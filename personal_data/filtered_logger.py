#!/usr/bin/env python3
""" Filtered logger module """
import re
from typing import List
import logging


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
        original = super().format(record)
        return filter_datum(
          self.fields, self.REDACTION, original, self.SEPARATOR)
