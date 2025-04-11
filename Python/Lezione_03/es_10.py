# Es. 10
somma = 0   
media = 0
counter = 0
dispari = 0
n = []

while True:
    n = []

    x = int(input("Inserisci un numero (0 per terminare): "))


    if x == 0:

        media = dispari / counter

        print(somma)
        print(media)

        break

    if x % 2 == 0:

        somma += x

    if x % 2 != 0:

        dispari += x
        counter += 1

    n.append(x)

for i in n:

    if i == i:

        print(i)
