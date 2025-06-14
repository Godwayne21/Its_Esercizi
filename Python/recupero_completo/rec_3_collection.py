'''
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''

def prod (x:dict[str,float])->dict[str,int]:

    diz = {}

    for prodotto,prezzo in x.items():

        if x[prezzo] < 50:

            diz[prodotto] = round(prezzo * 1.10 ,2)
        
    return diz