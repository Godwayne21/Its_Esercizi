#6
'''
3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45
'''

a = 2
b = 1
c = 30
d = 5

print('a)')
while True:
    if a <= 14:
        print(a)
        a += 2
    else:
        break
print('\n')
print('b)')
while True:
    if b <= 13:
        print(b)
        b += 3
    else:
        break

print('\n')
print('c)')
while True:
    if c >= 0:
        print(c)
        c -= 5
    else:
        break

print('\n')
print('d)')
while True:
    if d <= 45:
        print(d)
        d += 10
    else:
        break