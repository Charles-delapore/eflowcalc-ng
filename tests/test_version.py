"""Version smoke test."""

import re
import unittest

import eflowcalc


class VersionTest(unittest.TestCase):
    def test_version_is_a_string(self):
        self.assertIsInstance(eflowcalc.__version__, str)
        self.assertRegex(eflowcalc.__version__, r"^\d+\.\d+")

