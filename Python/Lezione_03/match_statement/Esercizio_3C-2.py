# Esercizio 3C-2
'''
Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi)
nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, 
espresso come numero intero e usare un match per determinare il corrispondente GPA americano, 
secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0
'''

x = int(input("Iserisci il voto: "))

match x:

    case x if x >= 106 | x <= 110:
        print (f"Voto Laurea: {x}\nGPA: 4.0")

    case x if x >= 101 | x <= 105:
        print (f"Voto Laurea: {x}\nGPA: 3.7")

    case x if x >= 96 | x <= 100:
        print (f"Voto Laurea: {x}\nGPA: 3.3")

    case x if x >= 91 | x <= 95:
        print (f"Voto Laurea: {x}\nGPA: 3.0")

    case x if x >= 86 | x <= 90:
        print (f"Voto Laurea: {x}\nGPA: 2.7")

    case x if x >= 81 | x <= 85:
        print (f"Voto Laurea: {x}\nGPA: 2.3")

    case x if x >= 76 | x <= 80:
        print (f"Voto Laurea: {x}\nGPA: 2.0")

    case x if x >= 70 | x <= 75:
        print (f"Voto Laurea: {x}\nGPA: 1.7")

    case x if x >= 66 | x <= 69:
        print (f"Voto Laurea: {x}\nGPA: 1.0")

    case _ :
        print("Voto non Valido")