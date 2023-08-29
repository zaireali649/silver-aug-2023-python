import random

# Generate a random number between 1 and 10 (inclusive)
number = random.randint(1, 10)

# Initialize a counter to keep track of attempts
counter = 0

# Repeat until the generated number is 7 or counter exceeds 12
while number != 7:
    number = random.randint(1, 10)  # Generate a new random number
    counter += 1  # Increment the counter for each attempt # counter = counter + 1
    if counter > 12:
        break  # Exit the loop if counter exceeds 12 attempts

# Print the number of attempts and the final generated number
print(counter, number)

# Iterate through numbers from 0 to 9 and print their squares
for i in range(10):
    print(i**2)
