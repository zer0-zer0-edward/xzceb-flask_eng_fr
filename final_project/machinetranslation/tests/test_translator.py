"""
This Python file is for unit testing the translator.py file
"""

import unittest

from translator import englishToFrench, frenchToEnglish

class englishToFrench(unittest.TestCase):
    def test_1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench(""), "")
    
class frenchToEnglish(unittest.TestCase):
    def test_1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(englishToFrench(""), "")

unittest.main()
