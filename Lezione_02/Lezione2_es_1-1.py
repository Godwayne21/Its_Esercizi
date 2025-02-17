#lezione 02 Esercizio 1-1:
x:float = 4.25
y:float = 1.0/x

print (f" il valore di x è: {x}\n Il valore di y è : {y: .2f}")

print(f"\n Il valore di x * y  è: {x*y}")

#modo 1
print (f"x*y-f= {x*y-x}")

#modo 2 
z:float = x*y
print(f"z-x= {z-x}")