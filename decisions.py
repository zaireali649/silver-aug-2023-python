import random

# Generate a random number between 0 and 10 (inclusive)
number = random.randint(0, 10)

# Set the threshold value for comparison
thresh = 4

# Compare the generated number with the threshold
if number > thresh: 
    print("Big Number")  # Print if the generated number is greater than the threshold
elif number < thresh: 
    print("Small Number")  # Print if the generated number is smaller than the threshold
else:  # In this case, number must be equal to thresh # elif number == thresh:
    print("Number is", thresh)  # Print if the generated number is equal to the threshold
    
# Print the generated random number
print(number)

