# Collections

# 1)Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, somma il valore al valore già associato alla chiave.

def convert(x:list[tuple])->dict:

    diz = {}

    for x,y in x:

        if x not in diz:
            diz[x] += y
        
        else:
            diz[x] = y
    
    return diz