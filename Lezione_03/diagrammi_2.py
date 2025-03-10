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

n_tutor =  10
attesa = 0

