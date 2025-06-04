#5
'''
Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
'''

def mol(x:list[int],threshold)->int:

    prod = 1

    for i in x:
        
        if i % 1 == 0 and i < threshold:
            prod *= i
        
        else:
            
            continue
    
    return prod

t = 5
num = [1,2,53,2]

print(mol(num,t))