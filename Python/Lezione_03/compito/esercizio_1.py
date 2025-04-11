''' Es.1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input,
terminando l'inserimento quando viene digitata la parola "fine" 
(che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e 
l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.
'''

while True:

    words = str(input("Write what you want ( write 'fine' if you want to stop): "))

    if words.lower() == "fine":
        break

    if words[0] == words[-1]:
        print ("The first and last letter are the same!")