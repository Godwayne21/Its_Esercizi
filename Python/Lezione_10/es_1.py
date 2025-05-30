'''
1. Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
Test case:
print(transform(4)) #  Output: 2
print(transform(-10)) #  Output: -5
'''

def transform(x:int)->int:

    if x % 2 == 0:
        return x / 2
    else:
        return x * 3 + 1
    
print(transform(4)) #  Output: 2
print(transform(-10)) #  Output: -5