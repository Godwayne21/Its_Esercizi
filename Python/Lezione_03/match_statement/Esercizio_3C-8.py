#Esercizio 3C-8
'''
Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.

Expected Output:
frase: di essere bellissimo
Output: Tu dici "di essere bellissimo"
- - - - - - - - - - - - - - - - - - - - - -
frase: ho vinto!
Output: Wow!
'''

parola = str(input("Scrivi una frase: "))

match parola:
    case parola if parola[-1] == "?" and len(parola) %2 == 0:
        print ("Si")
    
    case parola if parola[-1] == "?" and len(parola) %2 != 0:
        print ("No")
    
    case parola if parola[-1] == "!":
        print ( "Wow!")
    
    case _:
        print(f"Tu dici: {parola}")