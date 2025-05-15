'''
3. Sequenze di valori
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51
# Output:
Sequenza a):
1
2
3
4
5
6
7
'''

def sequenza(n:list[int])->int:
    for i in n:
        print(i)

print(f'Sequenza a)')
sequenza([1, 2, 3, 4, 5, 6, 7])
print(f'Sequenza b)')
sequenza([3, 8, 13, 18, 23])
print(f'Sequenza c)')
sequenza([20, 14, 8, 2, -4, -10])
print(f'Sequenza d)')
sequenza([19, 27, 35, 43, 51])