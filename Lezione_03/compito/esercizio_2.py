'''
Scrivere un programma che acquisisca una stringa inserita dall'utente e 
calcoli il numero totale di spazi presenti nella stringa. 
Il risultato deve essere visualizzato in output.
'''

x = str(input("Write what you want: "))

y : int = 0

for i in x:

    if i == " ":
        y += 1

print (f"There are {y} spaces!")