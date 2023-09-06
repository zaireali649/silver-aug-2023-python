# Import the 'os' module, which provides functions for interacting with the operating system
import os

# Define the file path as a string
path = "shapes.py"

# Use the 'os.path.exists()' function to check if the specified file exists in the given path
# This function returns True if the file exists, and False otherwise
print(os.path.exists(path))  # Print the result of the existence check
