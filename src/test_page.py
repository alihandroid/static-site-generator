import unittest

from page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
