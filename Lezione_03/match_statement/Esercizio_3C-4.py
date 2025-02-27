# Esercizio 3C-4
'''
Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, 
utilizzando un match statement, identifichi a quale categoria esso appartiene. 
L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,  
mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.

'''

mammiferi = ['cane', 'gatto', 'cavallo', 'elefante', 'leone']
rettili = ['serpente', 'lucertola', 'tartaruga', 'coccodrillo']
uccelli = ['aquila', 'pappagallo', 'gufo', 'falco']
pesci = ['squalo', 'trota', 'salmone', 'carpa']

animale = str(input("Che animale è? "))

match animale:
    case x if x in mammiferi:
        print (f"{x} è un mammifero")

    case x if x in rettili:
        print (f"{x} è un rettile")

    case x if x in uccelli:
        print (f"{x} è un uccello")

    case x if x in pesci:
        print (f"{x} è un pesce")
    
    case _:
        print("Non sono in grado di classificare l'animale inserito.")