# Es. 10
'''
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 
(che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta 
(cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
Esempio di input e output
Input:

Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0

Output:
Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)
'''

somma = 0
media = 0
x = 0
a = []
dispari = []
contatore = 0

while True :

    x = int(input("Inserisci un numero (0 per terminare): "))

    if x == 0:
        break

    a.append(x)

    if x % 2 == 0:
        somma += x
    
    if x % 2 != 0:
        dispari.append(x)
    
    for i in a:
        
        if i in a

media = sum(dispari) / len(dispari)


print("La media dei numeri dispari è : {media}")
print("La somma dei numeri pari è: {somma}")