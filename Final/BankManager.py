"""
@Author Jordan Dubreuil 05/05/2023
BankManager Class - Foundations of Programming
"""
from Account import *
from Bank import *
import random

class BankManager:
    def __init__(self):
        """
        Initializes the BankManager class.
        
        This is where you will implement your 'main' method and start
        the program from. The BankManager class should create an instance
        of a Bank object when the program runs and use that instance to
        manage the Accounts in the bank.
        
        Args:
            self: The BankManager instance.
        """
        bank = Bank()
        BankManager.promptForAccountNumberAndPIN(bank)
        
       
    @staticmethod  
    def promptForAccountNumberAndPIN(bank):
        
        """
        Prompts the user for an account number and PIN.

        Takes one parameter, a Bank object that represents the bank.
        The method should prompt the user to enter an account number
        and then try to find a matching account with that account number
        in the bank.

        Args:
            bank: A Bank object representing the bank.

        Returns:
            None
        """
        bank.mainmenu()
        return # be sure to change this as needed
    
    
    
if __name__ == "__main__":
    test = BankManager()


