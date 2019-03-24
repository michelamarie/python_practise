#!/usr/bin/python3

# make a function, put a parameter, divide the number by 10

import math

def divide(x):
    assert x >= 0, 'divide: bad input'
    return 10 / math.sqrt(x)

try:
    while True:
        try:
            divisor = input("Enter a non-zero divisor")

        except ZeroDivisionError:
            pass
            
        except AssertionError as error:
            print("Assertion error: ", error)
        
        except:
            print("An unknown exception has occurred.")

        finally:
            print("Interation complete. Beep, beep, boop.")

finally:
    print("That's all folks!")