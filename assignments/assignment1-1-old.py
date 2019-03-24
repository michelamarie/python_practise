#!/usr/bin/python3
# Assignment 1-1, by Michela Toscano

import math

numberlist = []
positives = []
negatives = []
answers = []
maxlistlength = 3

print("Please enter a number.")
number = float(input())
numberlist.append(number)



while len(numberlist) < maxlistlength:
    print('Thank you! Please enter another number.')
    morenumbers = float(input())
    numberlist.append(morenumbers)
    print (numberlist)

print('You have entered the following numbers:')
print (numberlist)

for i in numberlist:
    if i > 0:
        positives.append

for i in numberlist:
    if i <= 0:
        negatives.append

for i in positives:
    math.sqrt()
    answers.append

print('Shazam! Here are the square roots of all the positive numbers you have entered:')
print (answers)

print ('')

print('Square root for the follwing numbers could not be computed, because they are zero or negative.')
print (negatives)