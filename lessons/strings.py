#!/usr/bin/python3

# Write a routine that checks whether a string fits the following pattern:
# aaa-dddd-xxxxxx (True of False)

def check_string(string):
    first = string[0:3]
    second = string[4:8]
    third = string[9:17]
    #print(third)
    check_first = first.isalpha()
    check_second = second.isdigit()
    check_third = third.isalnum()
    
    
    # probably not needed: whole_thing = [check_first, check_second, check_third]

   
        

check_string('abc-1234-abc123')

print(Yay! The string given does fit the prescribed pattern.)
