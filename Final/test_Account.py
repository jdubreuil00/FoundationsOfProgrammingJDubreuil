"""
@Author Jordan Dubreuil 05/05/2023
test_Account Class - Foundations of Programming
"""
import unittest
from Account import Account

class test_Account(unittest.TestCase):

    def test_deposit_positiveAmount(self):
        account = Account()
        account.balance = 0
        deposit_amount = 100.50

        result = account.deposit(deposit_amount)

        self.assertEqual(result, 100.50)
    
    def test_deposit_negativeAmount(self):
        account = Account()
        account.balance = 50.75
        deposit_amount = -20.25

        result = account.deposit(deposit_amount)

        self.assertEqual(result, 50.75)

    def test_withdraw_sufficientFunds(self):
        account = Account()
        account.balance = 100.00
        withdraw_amount = 50.50

        result = account.withdraw(withdraw_amount)

        self.assertEqual(result, 49.50)
    
    def test_withdraw_insufficientFunds(self):
        account = Account()
        account.balance = 30.00
        withdraw_amount = 50.50

        result = account.withdraw(withdraw_amount)

        self.assertEqual(result, 30.00)

    def test_isValidPIN_validPIN(self):
        account = Account()
        account.pin = '1234'
        result = account.isValidPIN('1234')

        self.assertTrue(result)
    
    def test_isValidPIN_invalidPIN(self):
        account = Account()
        account.pin = '1234'
        result = account.isValidPIN('5678')

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
