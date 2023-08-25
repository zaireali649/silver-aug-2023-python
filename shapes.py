# Define a function 'area_of_triangle' that calculates the area of a triangle using given 'base' and 'height'.
def area_of_triangle(base, height):
    return base * height * 0.5  # Calculate and return the area using the formula: base * height * 0.5

# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Call the 'area_of_triangle' function with base 5 and height 11, and store the result in the 'area' variable.
    area = area_of_triangle(5, 11)

    # Print the calculated area to the console.
    print(area)
