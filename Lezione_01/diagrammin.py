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
massimo: int = int(input("Inserisci il primo valore: "))

count = 1

while count < 4:

    count += 1

    n: int= int(input("Inserisci altri valori: "))

    if n > massimo:

        massimo = n
    
    else:
        continue

print (f"Il numero più grande è: {massimo}")
'''

#repeat

'''
massimo: int = int(input("Inserisci il primo valore: "))

count = 1

while True:
    
    if count == 4:
        break
    else:    
        count += 1

        n: int= int(input("Inserisci altri valori: "))

        if n > massimo:

            massimo = n
        
        else:
            continue

print (f"Il numero più grande è: {massimo}")
'''

#for

'''
massimo: int = int(input("Inserisci il primo valore: "))

i = 0

for i in range(3):

    if i == 3:

        print (f"Il numero massimo è: {massimo}")
    
    else:
        
        i += 1

        n: int = int(input("Inserisci altri numeri: "))

        if n > massimo:

            massimo = n
        
        else:
            continue

print(f"Il numero massimo è: {massimo}")
'''