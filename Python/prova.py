def mcd(x:int, y:int)->int:

    if x > y:
        while y!= 0:
            x, y = y, x % y
        return abs(x)
        
    elif x < y:
        while x!= 0:
            y, x = x, y % x
        
        return abs(y)
        
    else:
        return 1

print(mcd(12, 18))  # Output: 6
print(mcd(7, 5))    # Output: 1 (perché 7 e 5 sono primi tra loro)
print(mcd(0, 5))    # Output: 5
print(mcd(0, 0))    # Output: 1 (caso limite)
print(mcd(48, 18))  # Output: 6