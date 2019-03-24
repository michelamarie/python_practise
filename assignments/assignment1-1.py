#!/usr/bin/python3
# Assignment 1-1, by Michela Toscano

import math


def square():
    numberlist = []
    positives = []
    negatives = []
    answers = []

    for i in range(1):
        try:
            print("Please enter a number.")
            number = float(input())
            numberlist.append(number)
        except ValueError:
            print("Doh! Please enter a numeral. No letters or blank responses allowed!")

    for i in range(2):
        try:
            print("Please enter another number.")
            morenumbers = float(input())
            numberlist.append(morenumbers)
        except ValueError:
            print("Doh! Please enter a numeral. No letters of blank responses allowed!")

    # Insert a line break in output to make it easier to read.
    print ('')

    print('You have entered the following numbers:')
    print (numberlist)

    print ('')

    for i in numberlist:
        if i > 0:
            positives.append(i)
        else:
            negatives.append(i)

    answers.append([math.sqrt(i) for i in positives])

    # Why doesn't this work (to do the same thing as above)?:
    #for i in positives:
    #    math.sqrt(i)
    #    answers.append(i)

    print('Shazam! Here are the square roots of all the positive numbers you have entered:')
    print(answers)

    print ('')

    print('Square root for the following numbers could not be computed, because they are zero or negative.')
    print (negatives)

square()
