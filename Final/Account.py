"""
@Author Jordan Dubreuil 05/05/2023
Account Class - Foundations of Programming
"""
import random


class Account:
    """
    A class representing a bank account.

    Attributes:
        _accountNumber (str): The account number.
        _firstName (str): The first name of the account owner.
        _lastName (str): The last name of the account owner.
        _ssn (str): The Social Security Number of the account owner.
        _pin (str): The PIN associated with the account.
        _balance (float): The account balance.

    Methods:
        accountNumber:
            Getter method for the account number.
        accountNumber.setter:
            Setter method for the account number.
        firstName:
            Getter method for the first name.
        firstName.setter:
            Setter method for the first name.
        lastName:
            Getter method for the last name.
        lastName.setter:
            Setter method for the last name.
        ssn:
            Getter method for the Social Security Number.
        ssn.setter:
            Setter method for the Social Security Number.
        pin:
            Getter method for the PIN.
        pin.setter:
            Setter method for the PIN.
        balance:
            Getter method for the account balance.
        balance.setter:
            Setter method for the account balance.
        deposit(amount):
            Deposits the specified amount into the account.
        withdraw(amount):
            Withdraws the specified amount from the account.
        isValidPIN(pin):
            Checks if the specified PIN is valid.
        __repr__():
            Returns a string representation of the account.

    """
    def __init__(self):
        self._accountNumber = None
        self._firstName = None
        self._lastName = None
        self._ssn = None
        self._pin = None
        self._balance = None

    # add methods as getters and setters for attributes
    @property
    def accountNumber(self):
        """
        Initializes an instance of the Account class.

        Args:
            self (Account): The Account instance.

        """
        return self._accountNumber

    @accountNumber.setter
    def accountNumber(self, accountNumber):
        """
        Getter method for the account number.

        Returns:
            str: The account number.

        """
        self._accountNumber = accountNumber

    @property
    def firstName(self):
        """
        Setter method for the account number.

        Args:
            accountNumber (str): The account number.

        Returns:
            None

        """
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        """
        Getter method for the first name.

        Returns:
            str: The first name.

        """
        self._firstName = firstName

    @property
    def lastName(self):
        """
        Setter method for the first name.

        Args:
            firstName (str): The first name.

        Returns:
            None

        """
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        """
        Getter method for the last name.

        Returns:
            str: The last name.

        """
        self._lastName = lastName

    @property
    def ssn(self):
        """
        Getter method for the Social Security Number.

        Returns:
            str: The Social Security Number.

        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """
        Setter method for the Social Security Number.

        Args:
            ssn (str): The Social Security Number.

        Returns:
            None

        """
        self._ssn = ssn

    @property
    def pin(self):
        """
        Getter method for the PIN.

        Returns:
            str: The PIN.

        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """
        Getter method for the account balance.

        Returns:
            float: The account balance.

        """
        self._pin = pin

    @property
    def balance(self):
        """
        Getter method for the account balance.

        Returns:
            float: The account balance.

        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """
        Setter method for the account balance.

        Args:
            balance (float): The account balance.

        Returns:
            None

        """
        self._balance = balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            float: The updated account balance.

        """
        if amount > 0:
            self._balance += amount
        return self._balance

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            float: The updated account balance.

        """
        if self.balance > amount:
            self._balance -= amount
        return self._balance

    def isValidPIN(self, pin):
        """
        Checks if the specified PIN is valid.

        Args:
            pin (str): The PIN to check.

        Returns:
            bool: True if the PIN is valid, False otherwise.

        """
        return pin == self._pin

    def __repr__(self):
        """
        Returns a string representation of the account.

        Returns:
            str: The string representation of the account.

        """
        line = ""
        for i in range(60):
            line += "="

        return f"{line} \nAccount Number: {self._accountNumber}\nOwner First Name: {self._firstName}\nOwner Last Name: {self._lastName}\nOwner SSN: xxx-xx-{self._ssn[-4:]}\nPIN:{self._pin}\nBalance:${self._balance:.2f}\n{line}"
