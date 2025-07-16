import math

def calculateCharges(ore:float)->float:
    prezzo:int = 0

    if ore < 3:
        prezzo = 2

    elif ore > 3 and ore < 24:

        prezzo = 2 + (math.floor(ore) -3)*0.5  # math.ceil per eccesso / math.floor per difetto

        if prezzo > 10:
            prezzo = 10
    
    else:
        prezzo = 10
    
    return prezzo

hours = [1.2 , 4, 5.5, 24]
charge = []

print (f"{'Cars':<5} {'Hours':<10} {'Charge $':<15}")

for index, value in enumerate(hours):
    num = index + 1
    cost = calculateCharges(value)
    charge.append(calculateCharges(value))

    print (f"{num:<5} {value:<10} {cost:<15.2f}")
