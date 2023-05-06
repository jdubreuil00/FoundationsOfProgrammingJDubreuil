from BankUtility import *
import unittest
import io
import sys
from unittest.mock import patch
from unittest.mock import Mock

class test_BankUtility(unittest.TestCase):
    @patch('builtins.input', return_value='test')
    def test_promptUserForStringValidInput(self, mockinput):
        result = BankUtility.promptUserForString("Please enter a word")
        self.assertEqual(result, 'test')
    
    @patch('builtins.input', return_value='')
    def test_promptUserForStringInvalidInput(self, mockinput):
        result = BankUtility.promptUserForString("Please enter a word")
        self.assertEqual(result, '')

    @patch('builtins.input', side_effect = ['-12', '0', '12'])
    def test_promptUserForPositiveNumberValidInput(self, mockinput):
        result = None
        while result is None:
            result = BankUtility.promptUserForPositiveNumber("Enter a valid number ")
        
        self.assertEqual(result, 12.0)
    
    def test_generateRandomInteger(self):
        # Test the range of generated random integers
        min_value = 1
        max_value = 10
        
        result = BankUtility.generateRandomInteger(min_value, max_value)
        
        self.assertTrue(isinstance(result, int))
        self.assertGreaterEqual(result, min_value)
        self.assertLessEqual(result, max_value)

    def test_convertFromDollarsToCents(self):
        # Test conversion of dollar amount to cents
        amount = 5.75
        expected_output = 575
        
        result = BankUtility.convertFromDollarsToCents(amount)
        self.assertEqual(result, expected_output)

    def test_isNumeric(self):
        # Test a numeric string
        numeric_string = "123"
        self.assertTrue(BankUtility.isNumeric(numeric_string))
        
        # Test a non-numeric string
        non_numeric_string = "abc"
        self.assertFalse(BankUtility.isNumeric(non_numeric_string))
    
  

if __name__=="__main__":
    unittest.main() 