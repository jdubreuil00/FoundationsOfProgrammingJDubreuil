"""
----Assignment 4 shapes.py----
@Author Jordan Dubreuil 04/11/2023
This program takes in user input for the length,
width, and depth of a rectangular volume. The file is divided
into two classes, Rectangle and the sub class Parallelepiped.
The Rectangle class has two methods that calculate Perimeter, and
Area and the Parallelepiped class extends the Rectangle class 
adding a method for calculating Volume. The main function requests
input for length, width, and depth, validates input then procedes to 
create instances of the Rectangle and Parallelepiped class and prints
the output data from their methods.
"""

class Rectangle:
    '''
    Creates the instance of a Rectangle from a length and width parameter

    Parameters:
        l(length):The length of the rectangle.
        w(width):The width of the rectangle.

    Returns:
        An instance of the Rectangle class  

    '''
    def __init__(self,l,w):
        '''
        Initializes the Rectangle class

        Parameters:
            l(length):The length of the rectangle.
            w(width):The width of the rectangle.

        Sets the properties for l and w. 
        '''
        self.l = l
        self.w =  w

    def Perimeter(self):
        '''
        Takes the length and width of the given rectangle and calculates the perimeter.

        Parameters:
            l(length):The length of the rectangle.
            w(width):The width of the rectangle.

        Returns:
            The perimeter of the rectangle.

        '''
        # formula for perimeter of rectangle.
        return 2*(self.l+self.w)
       

    def Area(self):
        '''
        Takes the length and width of the given rectangle and calculates the area.

        Parameters:
            l(length):The length of the rectangle.
            w(width):The width of the rectangle.

        Returns:
            The area of the rectangle.

        '''
        # formula for area of rectangle.
        return self.l*self.w
    
    def Display(self):
        """
        Prints the display output for the length, width, perimeter and area of the Rectangle.
        """
        print(f"The length of the rectangle is {self.l}.\nThe width of the rectangle is {self.w}.\nThe perimeter of the rectangle is {self.Perimeter()}.\nThe area of the rectangle is {self.Area()}.")
       

class Parallelepiped(Rectangle):
    '''
    Creates the instance of a Parallelepiped from a length, width, and depth parameter.
    Parallelepiped is a sub class of Rectangle.

    Parameters:
        l(length):The length of the parallelepiped.
        w(width):The width of the parallelepiped.
        d(depth):The depth of the parallelepiped.

    Returns:
        An instance of the Parallelepiped class  

    '''
    def __init__(self,l,w,d):
        '''
        Initializes the Parallelepiped class

        Parameters:
            l(length):The length of the parallelepiped.
            w(width):The width of the parallelepiped.
            d(depth):The depth of the parallelepiped.

        Sets the properties for l, w, and d. 
        '''
        super().__init__(l,w)
        self.d = d
        

    def Volume(self):
        '''
        Takes the length, width, depth of the given parallelepiped and calculates the volume.

        Parameters:
            l(length):The length of the parallelepiped.
            w(width):The width of the parallelepiped.
            d(depth):The depth of the parallelepiped.

        Returns:
            The volume of the parallelepiped.

        '''
        # formula for volume of parallelepiped.
        return (self.l*self.w)*self.d
    
    
    def Display(self):
        """
        Prints the display output for the Volume of the Parallelepiped.
        """
        print(f"The volume of the parallelepiped is {self.Volume()}.")
        



def main():
    # While loop validates user input
    while True:
        try:
            # Program asks for two positive floats l and w
            l = float(input("Please enter and length. "))
            w = float(input("Please enter and width. "))
            # Input for the parallelepiped d.
            d = float(input("Please enter the depth of the parallelepiped. "))

            
        except ValueError:
            #Validates input with a ValueError continues to and contiues to ask for input
            print('Sorry please try a valid number')
            continue
        if l < 0 or w < 0 or d <0:
            #Checks to see if l,w, and d are positive and continues to ask for input
            print('Please no negative numbers')
            continue
        else:
            # Creates instance of Rectangle.
            rect = Rectangle(l,w)
            # Call the Display Method from the instance of the Rectangle class. 
            rect.Display()
            # Creates instance of parallelepiped.
            para = Parallelepiped(l,w,d)
            # Call the Display Method from the instance of the Parallelepiped class. 
            para.Display()
            rect.Display()
            return False
               
if __name__=="__main__":
    main()