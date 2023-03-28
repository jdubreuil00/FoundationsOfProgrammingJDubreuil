import math

def evalInt():
    # While loop validates user input
    while True:
        try:
            # Program asks for two positive integers A and B
            a = int(input("Enter the first positive integer: "))
            b = int(input("Enter the second positive integer: "))
        except ValueError:
            #Validates input with a ValueError continues to and contiues to ask for input
            print('Sorry please try a valid number')
            continue
        if a < 0 or b < 0:
            #Checks to see if both inputs A and B are positive and continues to ask for input
            print('Please no negative numbers')
            continue
        else:
            #Input is valid run the function to check if evenly divisible
            break
    if a % b == 0 or b % a == 0:
        #Uses Modulus to check for remainder if no remainder print True Boolean. This condition checks for either order
        print(True)
        print(type(True))
    else:
        #There is a remainder and prints False Boolean
        print(False)
        print(type(False))
        evalInt()

#calls the function
evalInt()