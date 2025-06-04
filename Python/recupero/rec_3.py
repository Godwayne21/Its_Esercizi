#3
'''
Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''

def el(x:dict[str: int|float]) -> dict[str: int|float]:

    diz = {}

    for key,value in x.items():

        if value < 50:

            diz[key] = round(value * 1.10 , 2)

    return diz

print(el({"ton":51, "lib":21, "mutande":15.80}))