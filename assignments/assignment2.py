#!/usr/bin/python2
# Introduction to Python Programming: Assignment 2, Michela Toscano

# Notes:
# List structure: [key0, value0, key1, value1, key2, value2'].
# List length must be even (several sets of pairs of one key and one value -- len(l) % 2 == 0).
# Fuction must assert that keys may not be lists or a dictionary.

collection = []

# Instructions to user
print("Hello, friend. Please type in a list of names of people and their favourite number or colour. You may also enter a list of favourites in the form of 'x, y' (without the quotes).")
print("Enter a blank response when done.")
print("")

# Accept input from the user to build a list
def gather_info():
    while True:
        print("Please enter a name.")
        names = input()
        collection.append(names)

        print("Thank you!, Now please type that person's favourite number(s) and/or colour(s).")
        favourites = input()
        collection.append(favourites)

        if names == '':
            break

gather_info()

# print the list for testing. remove this later
#print(collection)

# Function which converts lists to dictionaries
def l2d():
    # I could not work out any other sensible way to do this. I had to look it up:
    dcollection = dict([(k, v) for k,v in zip(collection[::2], collection[1::2])])
    del dcollection['']
    print("You have entered the following names and corresponding favourites:")
    print(dcollection)

l2d()
