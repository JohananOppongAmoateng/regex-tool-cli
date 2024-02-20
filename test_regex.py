import unittest
import sys
from regex_cli import check_regex_validity

class TestCheckRegexValidity(unittest.TestCase):
    
    def setUp(self) -> None:
        self.regex = "^dog"
        self.string1 = "dogmatch"
        self.string2 = "snbandan"

    def test_regex_is_valid(self):
        self.assertTrue(check_regex_validity(self.regex,self.string1))

    def test_invalid_regex(self):
        self.assertFalse(check_regex_validity(self.regex,self.string2))


        