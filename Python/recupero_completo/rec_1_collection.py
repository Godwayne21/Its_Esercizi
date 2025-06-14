'''
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario.
Se la chiave è già presente, somma il valore al valore già associato alla chiave.
'''

def convert (x: list[tuple])-> dict:
    diz = {}

    for i in x:

        if i not in diz:
            key = i[0]
            value = i[1]
        
        if key in diz:
            diz[key] += [value]

        else:
            diz[key] = [value]
    
    return diz      