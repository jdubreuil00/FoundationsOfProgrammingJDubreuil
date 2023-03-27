import math

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
    if a<0 or b<0:
        #Checks to see if both inputs A and B are positive and continues to ask for input
        print('Please no negative numbers')
        continue
    else:
        #Input is valid run the function to check if evenly divisible
        break

# Returns if the two integers are divisible evenly
def evalInt(a,b):
    return a % b == 0 and b % a == 0

# Calls the function and prints the returned resiult
print(evalInt(a,b))

"""
Was not sure if the program should continue after validation and evalInt returns false.
From the wording of the assignment it seemed the progam only needed to ask for valid input.
"""