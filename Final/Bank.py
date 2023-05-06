"""
@Author Jordan Dubreuil 05/05/2023
Bank Class - Foundations of Programming
"""
from Account import *
import os
from BankUtility import *
from CoinCollector import *


class Bank:
    maxnumofaccounts = 100

    def __init__(self):
        """
        Initializes a Bank object.

        Creates an instance of the Bank class with an Null list of bank accounts. The
        maximum number of accounts is determined by the 'maxnumofaccounts' attribute.

        """
        self._bankaccounts = [None] * self.maxnumofaccounts

    def addAccountToBank(self, account):
        """
        Add an account to the bank.

        Args:
            account: An Account object to add to the bank.

        Returns:
            True if the account was successfully added.
            False if there are no more accounts available.

        This method iterates through the bank's accounts and adds the given account
        to the first empty slot. If there is no available slot, it prints a message
        indicating that no more accounts are available and returns False. If the
        account is successfully added, it returns True.
        """
        for item in range(len(self._bankaccounts)):
            if self._bankaccounts[item] == None:
                self._bankaccounts[item] = account
                return True
        print("No more accounts available")
        return False

    def removeAccountFromBank(self, account):
        """
        Removes the provided bank account from the bank's account list.

        Iterates through the list of bank accounts and checks if each account is
        equal to the provided account. If a match is found, the account is
        removed from the list by setting the corresponding element to None. Returns
        True if the account is successfully removed, and False if the account is not
        found.

        Parameters:
        account (BankAccount): The bank account object to be removed.

        Returns:
        bool: True if the account is successfully removed, False otherwise.

        """
        # implement removeAccountFromBank here
        for item in range(len(self._bankaccounts)):

            if self._bankaccounts[item] == account:
                self._bankaccounts[item] = None
                return True
        print("Bank account does not exist.")
        return False

    def findAccount(self, accountNumber):
        """
        Finds and returns a bank account based on the provided account number.

        Iterates through the list of bank accounts and compares the account number
        with the provided accountNumber. If a match is found, the corresponding
        account is returned. If no match is found, it prints a message stating that
        the bank account does not exist and returns None.

        Parameters:
        accountNumber (str): The account number to search for.

        Returns:
        BankAccount or None: The found bank account object if a match is found,
                            or None if no match is found.

        """
        for item in range(len(self._bankaccounts)):
            if self._bankaccounts[item] == None:
                break
            if self._bankaccounts[item].accountNumber == accountNumber:
                return self._bankaccounts[item]
        print("Bank account does not exist.")
        return None

    def addMonthlyInterest(self, percent):
        """
        Adds monthly interest to all bank accounts.

        Calculates and adds monthly interest to the balances of all bank accounts.
        The interest is calculated based on the provided interest rate percentage.
        Prints the new balance after adding the interest.

        Parameters:
        percent (float): The interest rate percentage to be applied to the account balances.                 
        """
        for item in self._bankaccounts:
           # interest calculation
           if item is not None:
            balance = item.balance
            decimal = percent/100
            payment = balance * decimal
            item.balance += payment
            print(
                f'Deposited interest: ${payment:.2f} into account number: {item.accountNumber}, new balance: ${item.balance:.2f}')
        self.mainmenu()
        # EXTRA CREDIT

    def hlinedraw(self):
        '''
        Returns a String that represents an ornamental line used in the Battleship Game Display Grid.

        Returns:
            line:The string which is the ornamental line used in the display grid.   

        '''
        # Defines the horzontal line of diplay grid
        line = ""
        for i in range(60):
            line += "="
        return line

    def displayScreen(self):
        """
        Displays the main menu of the bank.

        Prints the options available to the user, including various banking operations and program termination.
        Prints a horizontal line border before and after the menu options.
        
        """
        border = self.hlinedraw()
        bankOptionsList = ['What do you want to do?', '1. Open an account', '2. Get account information and balance', '3. Change PIN', '4. Deposit money in account', '5. Transfer money between accounts',
                           '6. Withdraw money from account', '7. ATM withdrawal', '8. Deposit change', '9. Close an account', '10. Add monthly interest to all accounts', '11. End Program']
        print(border)

        for i in bankOptionsList:
            print(i)

        print(border)

    def openAccount(self):
        """
        Opens a new account for a customer.

        Prompts the user to enter the account owner's first name, last name, and SSN (Social Security Number).
        Generates a random 4-digit PIN for the account.
        Generates a random 8-digit account number that does not already exist in the bank's account list.
        Creates a new Account object with the provided details and initializes the balance to 0.
        Adds the new account to the bank's account list.
        Prints the newly created account number and account details.
        Returns to the main menu.

        Note:
        - The generated PIN is a 4-digit number consisting of random digits between 1 and 4.
        - The generated account number is an 8-digit number consisting of random digits between 1 and 9.

        """
        while True:
            print('Open Account')
            firstname = input("Enter Account Owner's First Name: ")
            lastname = input("Enter Account Owner's Last Name: ")
            ssn = input("Enter Account Owner's SSN (9 digits): ")
            if len(ssn) != 9:
                print('Social Security Number must be 9 digits')
                self.mainmenu()
            pin = ''.join(str(BankUtility.generateRandomInteger(1, 9))
                          for _ in range(4))  # input("Create pin: ")
            newaccount = Account()
            accountNum = ''.join(random.sample('123456789', 8))
            newaccount.accountNumber = accountNum
            for account in self._bankaccounts:
                if account is not None:
                    while account.accountNumber == newaccount.accountNumber:
                        accountNum = ''.join(random.sample('123456789', 8))
                        newaccount.accountNumber = accountNum
                        print("Account matches")

            newaccount.firstName = firstname
            newaccount.lastName = lastname
            newaccount.ssn = ssn
            newaccount.pin = pin
            newaccount.balance = 0
            self.addAccountToBank(newaccount)
            print(newaccount.accountNumber)
            print(newaccount.__repr__())
            self.mainmenu()
            break

    def getAccount(self):
        """
        Retrieve and display the details of an account.

        This method prompts the user to enter an account number. If the account is found,
        it asks for the account's PIN. If the entered PIN is valid, it displays the
        account's details using the __repr__ method of the account object. If the PIN is
        invalid, it informs the user and returns to the main menu. If the account is not
        found, it informs the user and returns to the main menu.

        Returns:
            None
        """
        accountNum = input("Enter account number: ")

        account = self.findAccount(accountNum)
        if account != None:
            pin = input("Enter account PIN: ")
            if account.isValidPIN(pin):
                print(account.__repr__())
                self.mainmenu()
            else:
                print("Invalid PIN")
                self.mainmenu()
        else:
            print(f"Account not found for account number:  {accountNum}")
            self.mainmenu()

    def changePIN(self):
        """
        Change the PIN for an account.

        This method prompts the user to enter the account number for which the PIN should
        be changed. If the account is found, it prompts the user to enter the current PIN.
        If the entered PIN is valid, it asks the user to enter a new PIN and confirm it. If
        the new PIN matches the confirmation, it updates the account's PIN and displays a
        success message. Otherwise, it informs the user that the new PIN does not match and
        prompts for another attempt.

        Returns:
            None
        """
        accountNum = input("Enter account number: ")

        account = self.findAccount(accountNum)
        if account != None:
            pin = input("Enter account PIN: ")
            if account.isValidPIN(pin):
                while True:
                    newPIN = input('Enter new PIN: ')
                    newPINConfirm = input('Enter new PIN again to confirm: ')
                    if len(newPIN) != 4 or len(newPINConfirm) != 4:
                        print('PIN must be 4 digits, try again.')
                        continue
                    if newPIN == newPINConfirm:
                        account.pin = newPIN
                        print("PIN updated.")
                        break
                    else:
                        print("New PIN does not match try again")
                        continue

                self.mainmenu()
            else:
                print("Invalid PIN")
                self.mainmenu()
        else:
            print(f"Account not found for account number:  {accountNum}")
            self.mainmenu()

    def depositFunds(self):
        """
        Deposit funds into an account.

        This method prompts the user to enter the account number and PIN for the account
        to which funds will be deposited. If the account is found and the PIN is valid,
        it prompts the user to enter the amount to deposit in dollars and cents. It then
        performs the deposit by adding the specified amount to the account's balance. The
        new balance is displayed, and the method returns to the main menu.

        Returns:
            None
        """
        accountNum = input("Enter account number: ")
        account = self.findAccount(accountNum)
        if account != None:
            pin = input("Enter account PIN: ")
            if account.isValidPIN(pin):

                deposit = BankUtility.promptUserForPositiveNumber(
                    'Enter amount to deposit in dollars and cents (e.g. 2.57): ')
                account.deposit(deposit)
                print(f'New balance: {account.balance:.2f}')
                self.mainmenu()
            else:
                print("Invalid PIN")
                self.mainmenu()
        else:
            print(f"Account not found for account number:  {accountNum}")
            self.mainmenu()

    def transferFunds(self):
        """
        Transfer funds between two accounts.

        This method prompts the user to enter the account number and PIN for the account
        from which funds will be transferred. If the account is found and the PIN is valid,
        it prompts the user to enter the account number and PIN for the account to which
        funds will be transferred. If the second account is found and the PIN is valid, it
        prompts the user to enter the transfer amount in dollars and cents. It then
        performs the transfer by withdrawing the specified amount from the first account
        and depositing it into the second account. The new balances of both accounts are
        displayed, and the method returns to the main menu.

        Returns:
            None
        """
        print("Account to Transfer From:")
        accountNum1 = input("Enter account number: ")
        account1 = self.findAccount(accountNum1)
        if account1 != None:
            pin1 = input("Enter account PIN: ")
            if account1.isValidPIN(pin1):
                pass
            else:
                print("Invalid PIN")
                self.mainmenu()

        print("Account to Transfer To:")
        accountNum2 = input("Enter account number: ")
        account2 = self.findAccount(accountNum2)
        if account2 != None:
            pin2 = input("Enter account PIN: ")
            if account2.isValidPIN(pin2):
                pass
            else:
                print("Invalid PIN")
                self.mainmenu()
        transfer = BankUtility.promptUserForPositiveNumber(
            'Enter amount to transfer in dollars and cents (e.g. 2.57): ')
        account1.withdraw(transfer)
        account2.deposit(transfer)
        print("Transfer complete.")
        print(
            f'New balance in account:{account1.accountNumber} is: ${account1.balance:.2f}')
        print(
            f'New balance in account:{account2.accountNumber} is: ${account2.balance:.2f}')
        self.mainmenu()

    def withdrawFunds(self):
        """
        Withdraw funds from an account.

        This method prompts the user to enter an account number and PIN. If the
        account is found and the PIN is valid, it prompts the user to enter the
        withdrawal amount in dollars and cents. If the account has sufficient
        funds, the method withdraws the specified amount from the account,
        updates the account's balance, and displays the new balance. If the
        account has insufficient funds, an error message is displayed. After
        completion, it returns to the main menu.

        Returns:
            None
        """
        accountNum = input("Enter account number: ")
        account = self.findAccount(accountNum)
        if account != None:
            pin = input("Enter account PIN: ")
            if account.isValidPIN(pin):

                withdrawammount = BankUtility.promptUserForPositiveNumber(
                    'Enter amount to withdraw in dollars and cents (e.g. 2.57): ')
                if account.balance - withdrawammount >= 0:
                    account.withdraw(withdrawammount)
                    print(f'New balance: {account.balance:.2f}')
                    self.mainmenu()
                else:
                    print("Insufficient Funds")
                    self.mainmenu()
            else:
                print("Invalid PIN")
                self.mainmenu()
        else:
            print(f"Account not found for account number:  {accountNum}")
            self.mainmenu()

    def atmWithdraw(self):
        """
        Perform an ATM withdrawal from an account.

        This method prompts the user to enter an account number and PIN. If the
        account is found and the PIN is valid, it prompts the user to enter the
        withdrawal amount in dollars (without cents), which must be in multiples of
        $5 and not exceed $1000.

        If the withdrawal amount is valid and the account has sufficient funds, the
        method calculates the number of $20, $10, and $5 bills required to fulfill
        the withdrawal. It prints the breakdown of bills, updates the account's
        balance, and displays the new balance. If the withdrawal amount is invalid
        or the account has insufficient funds, appropriate error messages are
        displayed. After completion, it returns to the main menu.

        Returns:
            None
        """
        accountNum = input("Enter account number: ")
        account = self.findAccount(accountNum)
        if account != None:
            pin = input("Enter account PIN: ")
            if account.isValidPIN(pin):
                while True:
                    withdrawammount = BankUtility.promptUserForPositiveNumber(
                        'Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): ')
                    if withdrawammount >= 5 and withdrawammount <= 1000 and withdrawammount % 5 == 0:
                        if account.balance - withdrawammount >= 0:

                            twenty_dollars = withdrawammount // 20
                            ten_dollars = (withdrawammount % 20) // 10
                            five_dollars = (withdrawammount % 10) // 5

                            print(f"Number of $20 bills: {twenty_dollars}")
                            print(f"Number of $10 bills: {ten_dollars}")
                            print(f"Number of $5 bills: {five_dollars}")
                            account.withdraw(withdrawammount)
                            print(f'New balance: {account.balance:.2f}')

                            self.mainmenu()
                        else:
                            print("Insufficient Funds")
                            self.mainmenu()
                    else:
                        print("Invalid ammount, try again.")
            else:
                print("Invalid PIN")
                self.mainmenu()
        else:
            print(f"Account not found for account number:  {accountNum}")
            self.mainmenu()

    def depositChange(self):
        """
        Deposit change into an account.

        This method prompts the user to enter an account number and PIN. If the
        account is found and the PIN is valid, it prompts the user to enter a string
        representing the coins to deposit. Each character in the string represents a
        specific coin denomination ('P' for penny, 'N' for nickel, 'D' for dime,
        'Q' for quarter, 'H' for half-dollar, 'W' for whole dollar).

        The method calculates the total deposit amount based on the coins entered
        and adds it to the account's balance. It then prints the deposited amount
        and the updated balance. If the account or PIN is invalid, appropriate error
        messages are displayed. After completion, it returns to the main menu.

        Returns:
            None
        """
        accountNum = input("Enter account number: ")
        account = self.findAccount(accountNum)
        if account != None:
            pin = input("Enter account PIN: ")
            if account.isValidPIN(pin):
                coins = BankUtility.promptUserForString(
                    f"Deposit coins:\n 'P' represents a penny (1 cent)\n 'N' represents a nickel (5 cents)\n 'D' represents a dime (10 cents)\n 'Q' represents a quarter (25 cents)\n 'H' represents a half-dollar (50 cents)\n 'W' represents a whole dollar (100 cents)\n")
                print(coins.upper())
                coinsUpper = coins.upper()

                depositAmount = CoinCollector.parseChange(coinsUpper)
                account.balance += depositAmount
                print(f"{depositAmount:.2f} in coins deposited into account.")
                print(f"New balance is {account.balance:.2f}")
                self.mainmenu()
            else:
                print("Invalid PIN")
                self.mainmenu()
        else:
            print(f"Account not found for account number:  {accountNum}")
            self.mainmenu()

    def closeAccount(self):
        """
        Close an account in the bank.

        This method prompts the user to enter an account number and PIN to close
        the corresponding account. If the account is found and the PIN is valid,
        the account is removed from the bank's account list, and a confirmation
        message is printed. If the account is not found or the PIN is invalid,
        appropriate error messages are displayed. After completion, it returns to
        the main menu.

        Returns:
            None
        """
        accountNum = input("Enter account number: ")
        account = self.findAccount(accountNum)
        if account != None:
            pin = input("Enter account PIN: ")
            if account.isValidPIN(pin):
                self.removeAccountFromBank(account)
                print(f'Account {accountNum} closed')
                self.mainmenu()
            else:
                print("Invalid PIN")
                self.mainmenu()
        else:
            print(f"Account not found for account number:  {accountNum}")
            self.mainmenu()

    def addInterest(self):
        interestPercent = BankUtility.promptUserForPositiveNumber(
            'Enter annual interest rate percentage (e.g. 2.75 for 2.75%):')
        self.addMonthlyInterest(interestPercent)

    def mainmenu(self):
        """
        Display the main menu and handle user input.

        This method continuously displays the main menu screen until a valid choice
        is selected. It prompts the user for their choice and executes the
        corresponding functionality based on the selected option.

        Available options:
        1. Open an account
        2. Get an account
        3. Change PIN
        4. Deposit funds
        5. Transfer funds
        6. Withdraw funds
        7. ATM withdrawal
        8. Deposit change
        9. Close an account
        11. Exit the program

        Returns:
            None
        """
        while True:
            self.displayScreen()
            prompt = int(input("Enter your choice. "))
            if prompt < 0 or prompt > 11:
                print("Invalid choice. ")
                continue
            else:
                print(prompt)
                match prompt:
                    case 1:
                        self.openAccount()
                    case 2:
                        self.getAccount()
                    case 3:
                        self.changePIN()
                    case 4:
                        self.depositFunds()
                    case 5:
                        self.transferFunds()
                    case 6:
                        self.withdrawFunds()
                    case 7:
                        self.atmWithdraw()
                    case 8:
                        self.depositChange()
                    case 9:
                        self.closeAccount()
                    case 10:
                        self.addInterest()
                    case 11:
                        os._exit(0)
                break
