# Kristine Joy Barrina  #BSCPE 1-5  # April 23, 2023
# Creating a python program that will create two different files then square all even numbers and cube all odd numbers.

# Pseudocode

# Import python modules
import tkinter as tk
from tkinter import *
import os

# Open a file named integers.txt
with open ("integers.txt", "r") as integers:

    # Create a variable that contains all the integers
    integer_numbers = integers.readlines()
    
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

        # Open a file named triple.txt
        with open ("triple.txt", "a") as cube:
            
            # Append the cube value of odd integers to triple.txt
            cube.write (str(cube_odd) + "\n")
            
            # Apply loop control for odd cube numbers
            i += 1
        
# Design the output using tkinter
# Create an instance window
root = Tk ()

# Create the dimension of window
root.geometry("450x150")
root.title("Square of Even and Cube of Odd")

# Create a label click me
click_me_label = Label (root, text="Click here!", fg="black", justify=CENTER, font=("Arial", 14, "bold"))

#Create buttons
squared_button = Button (root, text="SQUARED EVEN NUMBERS", bg="yellow")
cube_button = Button (root, text="CUBE ODD NUMBERS", bg="yellow")

# Let the pack method declares the position attributes
click_me_label.pack ()
squared_button.pack ()
cube_button.pack()

tk.mainloop()

