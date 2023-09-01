import random

var = []  # Initializing an empty list

print(type(var))  # Printing the type of the variable 'var'

print(type("Hello World"))  # Printing the type of the string "Hello World"

var2 = [151, 251, 386, 493, 649, "009"]  # Creating a list 'var2' with mixed data types

print(var2)  # Printing the contents of 'var2'

var2.append(721)  # Appending the value 721 to 'var2' using the inplace function 'append'

print(var2)  # Printing the updated 'var2'

var2 = var2 + [1008]  # Concatenating a list with a single value [1008] to 'var2'

print(var2)  # Printing the updated 'var2'

number = random.randint(0, 10)  # Generating a random number between 0 and 10

print(dir(var2))  # Printing the list of attributes and methods of 'var2'

var2.reverse()  # Reversing the order of elements in 'var2'

print(var2)  # Printing 'var2' after reversing its elements

number = "52"  # Initializing a string 'number' with value "52"
print(type(number))  # Printing the type of 'number'
number = int(number)  # Converting the string 'number' to an integer
print(type(number))  # Printing the type of 'number' after conversion

numbers = range(1, 21)  # Creating a range object 'numbers' from 1 to 20
print(numbers)  # Printing the 'numbers' range object
print(type(numbers))  # Printing the type of the 'numbers' range object
numbers = list(numbers)  # Converting the range object 'numbers' to a list
print(numbers)  # Printing the contents of the 'numbers' list

for number in numbers:  # Looping through the 'numbers' list
    print(number**2)  # Printing the square of each number in the list

for i in range(0, 5):  # Looping through a range of numbers from 0 to 4
    print(i**3)  # Printing the cube of each number in the range

numbers.reverse()  # Reversing the order of elements in the 'numbers' list
print(numbers)  # Printing the 'numbers' list after reversing

print(numbers[5])  # Printing the value at index 5 in the 'numbers' list

print(len(numbers))  # Printing the length of the 'numbers' list

lol = [[0, 1, 2, 3],  # Creating a nested list 'lol'
       [0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3]
]

print(lol)  # Printing the contents of the nested list 'lol'

print(lol[2][3])  # Printing the value at row 2, column 3 in the 'lol' nested list

for i in lol:  # Looping through the outer list of 'lol'
    for j in i:  # Looping through the inner lists
        print(j)  # Printing each element in the inner lists
