'''
8.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente numeratore e denominatore.

Si definiscano i metodi __init__, setter, getter, __str__, value.
In particolare:
il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;
il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
i metodi setter devono controllare che il valore inserito sia un intero, in caso contrario il numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5. Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.
Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer() e isistance().
'''

class Frazione:

    def __init__(self,_numeratore:int, _denominatore:int):
        self._numeratore  (_numeratore)
        self._denominatore  (_denominatore)

    def set_numeratore(self,_numeratore)->None:

        if isinstance (_numeratore,int):
            self._numeratore = _numeratore
        
        else:
            self._numeratore = 13
        
    def set_denominatore (self, _denominatore)->None:

        if isinstance(_denominatore, int) and _denominatore > 0:
            self._denominatore = _denominatore
        
        else:
            self._denominatore = 5
    
    def get_numeratore (self)->int:
        return self._numeratore

    def get_denominatore (self)->int:
        return self._denominatore
    
    def __str__(self)->str:
        
        return f'{self._numeratore} / {self._denominatore}'
    
    def value (self)->float:

        return round (self._numeratore / self._denominatore, 3)

    def mcd(self,x:int,y:int)->int:

        divisore = 1

        lista = []

        if x > y:

            if x % divisore == 0:
                lista.append(divisore)
                divisore += 1
            
            else:
                