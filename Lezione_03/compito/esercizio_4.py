# Es. 4
'''
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi 
(sia interi che decimali). L'inserimento termina quando viene fornito un numero negativo, 
che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:
Calcolare la media dei soli numeri interi inseriti. 
Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti 
(sia interi che decimali).
'''

media = 0
i = 0
somma = []
numeri=[]
mass=0
minim=0
x = 0

while True:

    x = float(input("Write a number: "))

    if x < 0:
        break
    
    numeri.append(x)

    if x.is_integer():
        somma.append(x)
        i += 1
    
mass = max(numeri)
minim = min(numeri)

media = sum(somma) / i

print(f"la media è: {media}")
print(f"il numero più grande è: {mass}")
print(f"il numero più piccolo è: {minim}")