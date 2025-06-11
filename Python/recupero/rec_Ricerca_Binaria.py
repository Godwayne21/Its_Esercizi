'''
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno della lista, altrimenti False.
'''
def RicercaBinaria(num:int, lista:list)->bool:

    lista = sorted(set(lista))

    mid = len(lista) // 2

    if num > mid:
        for i in lista:
            if i <= lista[mid]:
                lista.pop(i)
            
            mid2 = len(lista) //2

            