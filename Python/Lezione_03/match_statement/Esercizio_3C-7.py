# Esercizio 3C-7
'''
Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T"
se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.
'''
testa = 0
croce = 0
lancio = 0

while lancio < 8:

    x = input("Inserisci 't' o 'T' per Testa e 'c' o 'C' per Croce? ").lower()

    lancio += 1

    match x:
        case "t" | "T":
            testa += 1
        
        case "c" | "C":
            croce += 1
        case _:
            print("Parola non riconosciuta. ")

            continue

somma = testa + croce

percentuale_testa = (testa/somma) * 100
percentuale_croce = (croce/somma) * 100

print(f"Totale 'testa': {testa}\nPercentaule 'testa': ({percentuale_testa:.2f})%")
print(f"Totale 'croce': {croce}\nPercentaule 'croce': ({percentuale_croce:.2f})%")