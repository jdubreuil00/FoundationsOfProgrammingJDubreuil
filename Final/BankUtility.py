"""
@Author Jordan Dubreuil 05/05/2023
BankUtility Class - Foundations of Programming
"""
import random


class BankUtility:

    def __init(self):
        pass

    @staticmethod
    def promptUserForString(prompt):
        # implement promptUserForString here
        stringData = input(f"{prompt} ")
        return stringData  # be sure to change this

    @staticmethod
    def promptUserForPositiveNumber(prompt):

        # implement promptUserForPositiveNumber here
        while True:

            doubleData = float(input(prompt))
            print(doubleData)
            if doubleData <= 0:
                print("Amount cannot be negative or zero. Try again.")
                continue
            else:
                return doubleData  # be sure to change this

    @staticmethod
    def generateRandomInteger(min, max):
        # implement generateRandomInteger here

        return random.randint(min, max)  # be sure to change as needed

    @staticmethod
    def convertFromDollarsToCents(amount):
        # implement convertFromDollarsToCents here
        amount = amount * 100
        return int(amount)  # be sure to change as needed

    '''
      Checks if a given string is a number (long)
      This does NOT handle decimals.
      
      YOU DO NOT NEED TO CHANGE THIS METHOD
      THIS IS FREE FOR YOU TO USE AS NEEDED
      
      @param numberToCheck String to check
      @return true if the String is a number, false otherwise
     '''
    @staticmethod
    def isNumeric(numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False
