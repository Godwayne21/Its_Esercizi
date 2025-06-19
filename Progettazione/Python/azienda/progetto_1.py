from custom_types import RealGEZ
from impiegato import *
from datetime import date,datetime

class Progetto:

    def __init__(self, nome: str, budget:RealGEZ, impiegati: set[Impiegato])->None:
        
        self.nome = nome
        self.budget = budget
        self.impiegati: set[Impiegato] = impiegati if impiegati is not None else set()
    
    def set_nome (self)->str:
        return self.nome
    
    def set_budget(self)->RealGEZ:
        return self.budget
    
    def add_Impiegato(self,impiegato)->None:
        if impiegato not in self.impiegati:
            self.impiegati.add(impiegato)
        
        else:
            raise FileExistsError("L'Impiegato è già presente")
    
    def remove_Impiegato(self,impiegato)->None:
        if impiegato in self.impiegati:
            self.impiegati.remove(impiegato)
        
        else:
            raise FileExistsError("L'Impiegato non è presente")
    
    