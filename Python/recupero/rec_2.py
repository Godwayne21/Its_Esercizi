#2
'''Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi
'''
def pos_neg(x:list[int|float])->dict[str:[int|float]]:

    diz={"pos":[], "neg":[]}

    for i in x:
        if i >= 0:
            diz["pos"].append(1)
        
        else:
            diz["neg"].append(i)
    
    return diz

print(pos_neg([1,-2,3]))



