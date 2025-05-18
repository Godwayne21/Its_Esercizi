'''
4. Integer Power
Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0. 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!
Test case: 
print(integerPower(3, 4)) # Output: 81
'''

def integerPower(b:int,e:int)->int:
    
    if b % 1 == 0 and e % 1 == 0 and e > 0:
        return b**e

print(integerPower(3, 4)) # Output: 81
