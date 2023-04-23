# Kristine Joy Barrina  #BSCPE 1-5  # April 23, 2023
# Creating a python program that will create two different files then square all even numbers and cube all odd numbers.

# Pseudocode

# Open a file named integers.txt
with open ("integers.txt", "r") as integers:

    # Create a variable that contains all the integers
    integer_numbers = integers.readlines()
    print (integer_numbers)
    
# Initialize variables that will store even and odd integers
even_integers = []
odd_integers = []

# Use for loop with range of all integers length
for i in range (len(integer_numbers)):

    # Check if integer is even 
    if (int(integer_numbers [i]) % 2) == 0:
        
        # Store even numbers in even_integers variable
        even_integers += integer_numbers [i]
        
        # Square even integer
        square_even = (int(integer_numbers [i])** 2)
        
        # Open a file named double.txt
        with open ("double.txt", "a") as squared:
            
            # Append the squared value of even integers to double.txt
            squared.write (str(square_even) + "\n")
    
             # Apply loop control 
            i += 1
            
    # Check if integer is odd 
    else:
        
        # Store odd numbers in even_integers variable
        odd_integers += integer_numbers [i]
        
        # Cube odd integer
        cube_odd = (int(integer_numbers [i])** 3)
        print (cube_odd)
        
        print ("it's odd!")

# Open a file named triple.txt
# Append the cubic value of odd integers to triple.txt
# Design the output using tkinter
