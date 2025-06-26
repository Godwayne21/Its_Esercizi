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

parcheggio = [1.2 , 4, 5.5, 24]

cars = [1,2,3,4]
print (f"{cars}")
for x in parcheggio:

