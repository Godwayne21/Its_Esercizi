'''
2. Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.
Test case:
print(calcola_stipendio(40)) # Output: 400.0
'''

def calcola_stipendio(x:int)->int:

    if x <= 40:
        return x * 10
    
    else:
        extra = x - 40
        normale = x -extra

        return extra * 15 + normale * 10

print(calcola_stipendio(40)) # Output: 400.0
print(calcola_stipendio(45)) # Output: 475.0