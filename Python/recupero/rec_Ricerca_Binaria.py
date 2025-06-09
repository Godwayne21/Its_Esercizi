'''
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno della lista, altrimenti False.
'''
def RicercaBinaria(num:int, lista:list)->bool:

    lista = sorted(set(lista))

    mid = len(lista) // 2

    meta = lista[:mid]

    if num > mid:

        if num < lista[-1]:

            lista2 = lista - meta
            mid2 = len(lista2) // 2
            meta_lista2 = lista2 [:mid2]
            
            if num > mid2:

                
        
        else:
            return False