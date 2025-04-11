# Es.7
'''
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, 
entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:
a[1] + b[n-1], a[2] + b[n-2], ...
Memorizzare ogni somma incrociata in una nuova lista c e, quindi, 
visualizzare in output le liste a, b, c.
'''

a = []
b = []
c = []
x = 0

while True:
    x = int(input("Put any number (put 0 to stop): "))

    if x == 0:
        break

    a.append(x)
    b.append(-x)
    c = a + b

print(a)
print(b)
print(c)