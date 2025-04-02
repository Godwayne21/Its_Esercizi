import math

def safe_sqrt(number):

    if number < 0:
        raise ValueError (f"The square root is negative")

    x = math.sqrt(number)
    print(f"The square root of {number} is {x}")

safe_sqrt(9)
safe_sqrt(-9)