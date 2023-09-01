import random

var = {}  # Initializing an empty dictionary 'var'

print(type(var))  # Printing the type of the variable 'var'

var2 = {"juice": "Cranberry",  # Creating a dictionary 'var2' with key-value pairs
        "movie": "The Lion King (1992)"}
        
print(var2)  # Printing the contents of the dictionary 'var2'

print(var2["movie"])  # Printing the value associated with the key "movie" in 'var2'

var2[0] = "Number"  # Adding a new key-value pair to 'var2'

print(var2[0])  # Printing the value associated with the key 0 in 'var2'

del var2[0]  # Deleting the key-value pair with key 0 from 'var2'

print(var2)  # Printing 'var2' after the deletion

var2["drank"] = "Patron"  # Adding a new key-value pair to 'var2'

print(var2)  # Printing 'var2' after adding the new pair

var2["drank"] = "CFA Lemonade (No Ice)"  # Modifying the value of an existing key

print(var2)  # Printing 'var2' after modifying the value

print(dir(var2))  # Printing the list of attributes and methods of 'var2'

print(var2.keys())  # Printing the keys of the dictionary 'var2'

print(var2.values())  # Printing the values in the dictionary 'var2'

for k, v in var2.items():  # Looping through key-value pairs in 'var2'
    print(k, v)  # Printing each key and its corresponding value
    
var3 = {"0": [0, 1, 2, 3],  # Creating a nested dictionary 'var3'
       "1": [0, 1, 2, 3],
       "2": [0, 1, 2, 3],
       "3": [0, 1, 2, 3]
}

for k, v in var3.items():  # Looping through key-value pairs in 'var3'
    print(k, v)  # Printing each key and its corresponding list
    
    for i in v:  # Looping through elements in the list 'v'
        print(k, i)  # Printing the key and each element in the list
