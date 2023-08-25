# Import the 'random' module to generate random numbers and 'os' module for operating system-related functions.
import random 
import os

# Import the 'shapes' module which presumably contains the 'area_of_triangle' function.
import shapes

# Generate a random integer between 1 and 10 (inclusive) and assign it to the variable 'base'.
base = random.randint(1, 10)

# Generate another random integer between 1 and 10 (inclusive) and assign it to the variable 'height'.
height = random.randint(1, 10)

# Calculate the area of the triangle using the imported 'area_of_triangle' function with the random 'base' and 'height'.
area = shapes.area_of_triangle(base, height)

# Print the values of 'base', 'height', and 'area' to the console.
print(base, height, area)
