import math

while True:
    try:
        a = int(input("Enter the first positive integer: "))
        b = int(input("Enter the second positive integer: "))
    except ValueError:
        #Validate input
        print('Sorry please try a valid number')
        continue
    if a<0 or b<0:
        print('Please no negative numbers')
        continue
    else:
        break

def evalInt(a,b):
    if a % b == 0 and b % a == 0:
        print("True")
    else:
        print("False")


evalInt(a,b)