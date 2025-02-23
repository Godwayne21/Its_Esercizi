'''
Scrivere un programma che acquisisca una stringa inserita dall'utente e 
generi una nuova stringa che corrisponda alla versione invertita della stringa originale.
Il programma deve poi visualizzare la stringa ottenuta in output. 
Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.
'''

x = str(input("What do you want to reverse? "))

y:str = str()

for i in range(len(x) -1,-1,-1):

    y += x[i]

print (y)