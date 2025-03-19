def sumInRange(a:int,b:int)->None:

    #scambio i valori
    if a > b:
        x:int = a
        a = b
        b = x
    #secondo modo
        #a,b=b,a

    sum = 0

    while b >= a:

        sum += a
        a += 1

    print(sum)

    return int(sum)

sumInRange(5,10)
sumInRange(10,5)