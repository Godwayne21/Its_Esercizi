# 2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che classifichi i numeri in liste separate per numeri positivi e negativi.

def pos_neg (x:list[int])->dict:

    diz = {'pos': [], 'neg': []}

    for i in x:


        if i >= 0:
            diz['pos'].append(i)
            
        else:
            diz['neg'].append(i)

    return diz
    