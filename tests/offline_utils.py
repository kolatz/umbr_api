#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import os
import unittest
from ast import literal_eval


# pylint: disable=R0903
class FakeResponse:
    """To mimic ``requests`` response obj."""

    def __init__(self, case_dir):
        """Create fake class."""
        status_code_file = os.path.join(
            os.path.dirname(__file__), case_dir, "code.txt"
        )
        body_file = os.path.join(
            os.path.dirname(__file__), case_dir, "body.json"
        )
        headers_file = os.path.join(
            os.path.dirname(__file__), case_dir, "headers.json"
        )
        with open(status_code_file) as file:
            self.status_code = int(file.read())
        with open(headers_file) as file:
            self.headers = literal_eval(file.read())
        with open(body_file) as file:
            self.text = file.read()
        # pylint: disable = C0103
        self.ok = bool(self.status_code >= 200 or self.status_code < 400)


if __name__ == "__main__":
    unittest.main()
