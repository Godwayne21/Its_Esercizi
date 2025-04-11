# 1
'''
max_posti = int(input("Inserisci numero di posti: "))

liberi = max_posti

while True:

    opzione = str(input("Scegli tra: 'ingresso', 'uscita', 'stato' e 'esci': "))

    if opzione == 'ingresso':

        if liberi > 0:
            
            liberi -= 1
        
        else:
            print ('non ci sono posti liberi')

    if opzione == 'uscita':

        if liberi < max_posti:

            liberi += 1

        else:
            print('tutti i posti sono già disponibili')
    
    if opzione == 'stato':

        print(f'i posti liberi sono: {liberi}')

        print(f'i posti ocpati sono: {max_posti - liberi}')
    
    if opzione == 'esci':

        break
'''

# 2
'''
nord_sud = int(input("Quanti macchine nord_sud? "))
est_ovest = int(input("Quanti macchine est_ovest? "))
soglia = 70

    
if nord_sud > soglia and est_ovest > soglia:

    time_ns = 50
    time_eo = 50
    
elif nord_sud > soglia:
    time_ns = 60
    time_eo = 40
    
elif est_ovest > soglia:
    time_ns = 40
    time_eo = 60
    
else:
    time_ns = (nord_sud/(nord_sud + est_ovest)) * 100
    time_eo = (est_ovest/(nord_sud + est_ovest)) * 100


print(f"Il tempo assegnato a Nord-Sud è: {time_ns}")
print(f"Il tempo assegnato a Est-Ovest è: {time_eo}")
'''

# 3
'''
max_posti = 100

while True:
    nome_corso = str(input("Inserisci il nome del corso: "))

    opzione = str(input("Scegli tra: 'iscrivi', 'annulla', 'visualizza', 'elimina', 'esci': "))

    match opzione:

        case 'iscrivi':

            if max_posti > 0:
                max_posti -= 1   
            
            else:
                print("non ci sono posti disponibili")
        
        case 'annulla':

            if max_posti:
                max_posti += 1
            
            else:
                print("tutti i posti sono già disponibili")
        
        case 'visualizza':
            
            print(f'I posti liberi sono: {max_posti}')
            print(f'I posti occupati sono: {100 - max_posti}')
        
        case 'elimina':
            nome_corso = str(input("Inserisci il nome del corso: "))
        
        case 'esci':
            break

        case _:
            print ("Comando non riconosciuto.")
'''
# 4
'''
n_tutor =  10
attesa = 0

while True:

    studente = str(input("Nome? "))

    if n_tutor > 0:

        n_tutor -= 1

        print("Tutor assegnato con successo")
    
    else:

        attesa += 1

        print("Studente in attesa")
    
    if n_tutor == 0 and attesa > 50:

        break
    else:
        continue
'''

# 5
'''
n = int (input("Inserisci un numero: "))

while True:

    if n % 1 == 0 and n > 0:

        somma = 0
        i = 1

        while i < n:
            somma += i *i

            i += 1
        else:
            print(f"La somma è {somma}")

            break

    else: 

        print("Errore, n deve essere positivo.")
        break 
'''

# 6
'''
x = int(input("Inserisci un numero: "))
somma = 0

if x > 0:
    i = 0

else:
    print("Errore, x deve essere positivo.")

while i!= 10:

    n = int(input("Inserisci un altro numero: "))

    if x % 2 == 0:
        if n > x/2:

            somma += n
        
        else:
            if n < x:
                somma += n
        
        i += 1

else:
    print(f"La somma è {somma}")
'''

# 7
'''
cont = 0
somma = 0

while True:

    scelta = str(input("Vuoi inserire in voto? "))

    match scelta:
        
        case scelta if scelta == 'sì' or 'si':

            voto =int(input("Inserisci il voto: "))

            if voto > 0:

                cont += 1

                somma += voto

            else:
                print("Errore")
    
        case scelta if  scelta == 'no':

            if cont > 0:
            
                media = somma/cont

                print(f"La media è: {media}")
        
            else:
                print("Nessun voto inserito.")

            break
'''
# 8
'''
a = int(input("Inserisci un numero: "))
b = int(input("Inserisci un altro numero: "))

if a < b:
    if a > 0 and b:
        if a % 1 == 0 and b % 1 == 0:
            somma = 0
            i = a

            while True:

                if i > b:
                    print(f"La somma è {somma}")
                    break 

                else:
                    somma += i
                    i += 1
        else:
            print("a e b devono essere interi")
    else:
        print("a e b devono essere positivi")
else:
    print("a deve essere minore di b")
'''

# 9
'''
n = int(input("Inserisci un numero: "))
while True:

    if n > 0:

        if n % 1 == 0:
            cont = 0
            i = 0

            while i != 0:

                x = int(input("Insert a number: "))

                if x % n == 0:

                    cont +=1
                
                i += 1
                print(f"I numeri divisibili per {n} sono {cont}")

                break
        
        else:
            print("n deve essere intero positivo")
            n = int(input("Inserisci un altro numero: "))
    
    else:
        print("n deve essere positivo")
        break
'''

# 10

