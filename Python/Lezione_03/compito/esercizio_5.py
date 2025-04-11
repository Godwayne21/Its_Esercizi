# Es. 5
'''
Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro 
ciascuna. Ogni barretta acquistata contiene un buono sconto, 
e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:
Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, 
considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.
'''

n = int(input("Quanti soldi hai? "))
tot = 0
buoni = 0

while True:

    if n == 0:
        break

    if n % 6 == 0:
        tot += 1
        buoni -= 1

    n -= 1
    tot += 1
    buoni += 1

print(f"Il numero di barrette ottenute sono: {tot}")
print(f"I buoni rimasti sono: {buoni}")