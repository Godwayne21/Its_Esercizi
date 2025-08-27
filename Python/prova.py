def mcd(x:int, y:int)->int:

    while y:

        x,y = y, x % y
    
    return x


print(mcd(12,18))