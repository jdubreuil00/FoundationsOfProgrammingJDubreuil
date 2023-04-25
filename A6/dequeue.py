"""
@Author Jordan Dubreuil 04/23/2023
Assignment 6 Dequeque Abstract Data Type.
"""


class Dequeque:
    '''
    Creates a unique instance of a double ended queue implemented as an abstract data type. 
    This ADT is used to capture a list of food.

    Parameters:
        none

    Returns:
        An instance of the Dequeque class  

    '''

    def __init__(self):
        '''
        Initializes the Dequeque Class

        Parameters:
            none

        Returns:
            A food list for the double ended queue

        '''
        self.food = []

    def IsEmpty(self):
        '''
        Checks to see if the double ended queue is empty

        Parameters:
            none

        Returns:
            True if dequeque is empty, False if it is not. 

        '''
        return self.food == []

    def addEnd(self, item):
        '''
        Adds food item to the end of the queue

        Parameters:
            item(string): name of food.

        Returns:
            nothing

        '''
        self.food.append(item)

    def addStart(self, item):
        '''
        Adds food item to the start of the queue

        Parameters:
            item(string): name of food.

        Returns:
            nothing

        '''
        self.food.insert(0, item)

    def display(self):
        '''
        Prints food items in the queue

        Parameters:
            none

        Returns:
            Print of food items in the queue.

        '''
        print(self.food)


def main():
    '''
    Main function requests user to add food items or enter Q to quit and 
    display the queue

    Parameters:
        none

    Returns:
        Prints food items in the queue

    '''
    # Creates instance of Dequeque.
    foodItems = Dequeque()

    while True:
        # Asks for the user to enter food item or enter Q to display the dequeque.
        data = input(
            "Enter in a food or type Q to exit and display the dequeque. ")

        # If Q is entered exit the program
        if data == "Q":
            # Calls display to print the queque.
            foodItems.display()
            break

        # Checks to see if food items is empty. If it is add in the food item.
        if foodItems.IsEmpty():
            foodItems.addEnd(data)
            foodItems.display()
            pass

        # If there are items in the queue prompt the user where to enter the food item in the queue.
        else:
            while True:
                side = input(
                    "Enter which side of the dequeque, start or end. ")
                if side == "start":
                    # Adds to the start of the queue.
                    foodItems.addStart(data)
                    foodItems.display()
                    break
                elif side == "end":
                    # Adds to the end of the queue.
                    foodItems.addEnd(data)
                    foodItems.display()
                    break
                else:
                    # If the user prompt is incorrect please reenter the prompt.
                    print("Please enter start or end. ")
                    continue


# Enters the main function
if __name__ == "__main__":
    main()