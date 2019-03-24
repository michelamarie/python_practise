#!/usr/bin/python3

# make a function, put a parameter, divide the number by 10

import math

def divide(x):
    assert x >= 0, 'divide: bad input'
    return 10 / math.sqrt(x)

try:
    for i in range(5):
        try:
            n = int(input())
            print(divide(n))

        except AssertionError as error:
            print("Assertion error: ", error)

        except ZeroDivisionError:
            pass
        
        #except

        finally:
            print("Interation complete. Beep, beep, boop.")

finally:
    print("That's all folks!")