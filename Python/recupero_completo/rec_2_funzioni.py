'''
2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
'''

def molt(x:list[int|float], t:int)->int:

    prodotto = 1

    for i in x :

        if i % 1 == 0 and i < t:

            prodotto *= i
    
    return prodotto

print (molt([1,3,2,1.2],3))