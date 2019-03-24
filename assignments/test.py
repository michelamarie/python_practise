#!/usr/bin/python3

import re

print("Please enter a number.")
number = input()

def isphone():
    numtocheck = re.compile(r'\d{3}-\d{3}-\d{4}')
    numtocheck.search(number).group()
    