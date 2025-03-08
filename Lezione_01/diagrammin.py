#1
'''
a: float= float(input("Inserisci a: "))
b: float= float(input("Inserisci b: "))

if a > b:

    c: float = (a**2 - b**2)**0.5

    print(f"C è: {c}")

else:
    print("Errore")
'''

#2

#while
'''
massimo: float = float(input("Inserisci il primo valore: "))

count = 1

while count < 4:

    count += 1

    n: infloatt= float(input("Inserisci altri valori: "))

    if n > massimo:

        massimo = n
    
    else:
        continue

print (f"Il numero più grande è: {massimo}")
'''

#repeat

'''
massimo: float = float(input("Inserisci il primo valore: "))

count = 1

while True:

        n: float= float(input("Inserisci altri valori: "))

        if n > massimo:

            massimo = n
        count+=1

        if count == 4:
            break        
        

print (f"Il numero più grande è: {massimo}")
'''

#for

'''
massimo: float = float(input("Inserisci il primo valore: "))

for i in range(3):
    
    n: float = float(input("Inserisci altri numeri: "))
    
    if n > massimo:

        massimo = n


print(f"Il numero massimo è: {massimo}")
'''

#3
'''
somma = 0

count = 0

while True:

    n:float= float(input("Inserisci un numero: "))

    if n > 0:

        somma += n
    else:
        continue

    count += 1

    if count > 5:
        break

print(f"La somma totale è: {somma}")
'''

#4
'''
n: float = float(input("Inserisci un numero: "))

if n % 2 == 0:

    print(f"Il numero {n} è pari")

else:
    print(f"Il numero {n} è dispari")
'''

#5

'''
n:int= int(input("Inserisci un numero: "))

is_prime = True

if n < 2:
    is_prime=False

else:
    div = 2

    while div < n:

        if n % div == 0:

            is_prime = True
        
        else:
            div += 1
    
    else:
        is_prime = False

if is_prime == True:

    print (f"{n} è un numero primo")

else:
    
    print (f"{n} è un numero primo")
'''

# 6

n:float = float(input("Insert a number: "))

while n % 1 == 0 and n > 0:

    fattoriale = 1

    i = 1

    if i == n:
        print
    
    else:

        fattoriale *= i

        i += 1