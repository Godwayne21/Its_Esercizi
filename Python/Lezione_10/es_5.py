'''
5. Teorema di Pitagora
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.
Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
Test case:
print(hypotenuse(3.0, 4.0)) # Output: 5.0
'''

def hypotenuse(x:float, y:float) -> float:

    return (x**2 + y**2) * 0.5

print(hypotenuse(3.0, 4.0)) # Output: 5.0