import random

"""
    -------BATTLESHIPS-------
    Design: GK 
    Program Developed by: Jordan Dubreuil 04/04/2023
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How it will work:
    1. A 10x10 grid will have 5 ships randomly placed about
    2. You can choose a row and column to indicate where to shoot
    3. For every shot that hits or misses it will show up in the grid
    4. If all ships are shot, game over

    Legend:
    1. "." = water
    2. "S" = ship position
    3. "O" = water that was shot with bullet, a miss because it hit no ship
    4. "X" = ship sunk!
"""

# Global variable for grid size.
grid_size = 10
# Global variable for grid.
grid = [ ['']*grid_size for i in range(grid_size) ]
# Global variable for number of ships to place.
num_of_ships = 5

def hlinedraw():
    '''
    Returns a String that represents an ornamental line used in the Battleship Game Display Grid.

    Returns:
        line:The string which is the ornamental line used in the display grid.   

    '''
    # Defines the horzontal line of diplay grid
    line = ""
    for i in range(grid_size + 1):
        line += "+"
        for j in range(3):

                line += "-"
    line += "+"
    return line



def drawBoard():
    '''
    Prints the display output grid to for the user in the console.

    Prints:
        Prints to each line of the console the display grid and the array of ships 
        with X (column) and Y (row) coordinates.   

    '''
    # Keeps track of the number of times game data is drawn to the grid.
    data = 0
    # Runs the function that prints the horizontal line of the grid.
    hline = hlinedraw()
    # Prints the first line of the display grid.
    print(hline)
    # Composes the numbered row of columns at the top of the display grid.
    line2 = ""
    for num in range(grid_size + 1):
        line2 += "|"
        if num > 0:
            line2 += " " + str(num - 1) + " "
        else:
            line2 += " " + " " + " "
        num += 1
    line2 += "|"
    # Prints the row ofnumbers at the top of the display grid.
    print(line2)
    # This for loop checks for every other line, if even it draws the horizontal line, odd it draws the game data from the array.
    for i in range(grid_size * 2):
        if i%2  == 0:
            # even row draws lines
            print(hline)
        else:
            # odd row draws game data
            line2 = ""
            line2 += "|"
            for col in range(len(grid)+1):
                if col == 0:
                    line2 += " " + str(data) + " |"
                else:  
                    line2 += " " + str(grid[data][col-1]) + " |"
            # Increments the data line for the row values (Y) of the display grid and from the array.
            data += 1
            #  Prints the Row to the display grid output.  
            print(line2)
    # Prints the final horizontal line to the display grid.
    print(hline)



def setupBoard(thearray):
    '''
    Initializes the game board for the Battleship game.

    Parameters:
        thearray (array):Two dimensional array of values built with the grid_size 10X10.

    Returns:
        Returns no data and sets the empty spots in the array to '.' and places 
        the ships 'S' at random positions.  

    '''
    # initialize all grid[i][j] = '.'
    i = j = 0
    while i < grid_size:
        while j < grid_size:
            # Store the string "i, j" into the array.
            thearray[i][j] = "."
            j += 1
        j = 0
        i += 1
    # Place the ships at random positions in the array.
    for ship in range(num_of_ships):
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)
        while thearray[randomRow][randomCol] == "S":
            randomRow = random.randint(0, grid_size - 1)
            randomCol = random.randint(0, grid_size - 1)
        thearray[randomRow][randomCol] = "S"
        

def checkHitOrMiss(myBoard, row, col):
    '''
    Returns Hit or Miss based off of the parameters row and col passed to the funtion.

    Parameters:
        myBoard (array): Two dimensional array, 10x10 grid that represents the game board.
        row (int): Represents the row entered by the user.
        col (int): Represents the column entered by the user.

    Returns:
        Hit(str1): String "Hit" if user selects a coordinate that has a ship.   
        Hit(str2): String "Hit" if user selects a coordinate that has previously hit a ship.   
        Miss(str2): String "Miss" if user selects a coordinate that does not have a ship.   

    '''
    # Checks to see if the attempt was a hit.
    if myBoard[row][col] == "S":
        # Prints hit.
        print("Hit")
        # Changes the entry to an X in the array
        myBoard[row][col] = "X"
        return "Hit"
    # Else if entry alreay has been hit.
    elif myBoard[row][col] == "X": 
        print("Hit") 
        return "Hit"
    # User entry does not contain a ship therefore is a MISS
    else:
         # Print Miss
        print("Miss")
        # Changes the entry to an O in the array
        myBoard[row][col] = "O"
        return "Miss"
    

def isGameOver(myBoard):
    '''
    Returns True is all of the ships in the myBoard have been hit and returns false if they have not.
    This method is responsible for playing the game until all the ships have been hit.

    Parameters:
        myBoard (array):Two dimensional array that contains all the coordinates for ships in the game.

    Returns:
        True(bool):Boolean True is returned if all the ships in the array have been hit.
        False(bool):Boolean False is returned if there are ships remaining in the array that have not been hit.  

    '''
    # Check if there are ships remaining on the grid.
    # If there are ships remaining, return false else return true
    shiphit = 0
    for col in range(grid_size):
        for row in range(grid_size):
            if myBoard[row][col] == "X":
                shiphit += 1
    # If ships hit is equal to the number of the ships in game, return True.
    if shiphit == num_of_ships:
        # Game Over exits the while loop
        return True
    # Else there are ships left continue the game.
    else:
        return False

def main(myBoard):
    '''
    Core loop of the Battleship game.
    1. Sets up the two dimensional array for the game board.
    2. Outputs the game board to the console.
    3. Asks for user input for the Column(X) value.
    4. Asks for user input for the Row(Y) value.
    5. Checks if the users entry was a hit or a miss.
    6. Checks if there are ships left in the game. 
       If none are left GAME OVER. If there are ships remaining continue

    Parameters:
        myBoard (array):Two dimensional array that contains all the coordinated for ships in the game.

    Returns:
        True(bool):Boolean that returns True if all the ships have been hit, exiting the core game loop.  

    '''
    #Sets up the 2D Array for the Game Board
    setupBoard(grid)
    #While loop checks the game logic.
    while True:
            # Prints the board to the console.
            drawBoard()
            # Takes the console Input.
            col = input("Please enter a column (X): ")
            # Checks to see if the column is a numeric value.
            if col.isnumeric():
                # Casts the input to an integer.
                col = int(col)
                # Checks if the column input is between 0 and 9. 
                if col < 0 or col >=10:
                    # Prints Invalid column if the range is incorrect. Asks to reenter the column.
                    print("Invalid column.")
                    continue
                # If column passes asks for the row input.
                row = input("Please enter a row (Y): ")
                # Checks to see if the row is a numeric value
                if row.isnumeric():
                    # Casts the input to an integer.
                    row = int(row)
                    # Checks if the row input is between 0 and 9.
                    if row < 0 or row >=10:
                        # Prints Invalid row if the range is incorrect. Asks to reenter the column from the beginning
                        print("Invalid row.")
                        continue
                    # If both the row and column are valid, checks to see if the selection hits a ship.
                    checkHitOrMiss(grid, row, col) 
                    # Checks to see if the number of ships is 0.
                    if isGameOver(grid):
                        # Game Over exits the while loop
                        drawBoard()    
                        print('GAME OVER!')
                        return True
                     # Else there are ships left continue the game
                    else:
                        pass 
                else:
                #   Row is an invalid entry.
                  print("Please enter a valid number") 
            else:
                # Column is an invalid entry.
                print("Please enter a valid number")        
    
    
# Call to main to start the game.
if __name__=="__main__":
    main(grid) 

