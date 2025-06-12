from custom_types import RealGEZ
from impiegato import *
from datetime import date

class Progetto:
    
    def __init__(self, nome:str, budget:RealGEZ)->None:
        
        self.nome = nome
        self.budget = budget
        self.impiegati = {}
    
    def get_nome (self)->str:
        return self.nome
    
    def get_budget(self)-> RealGEZ:
        return self.budget
    
    def add_imp (self,impiegato,data)->None:
        if impiegato not in self.impiegati:
            self.impiegati[impiegato] = data
        
        else:
            raise KeyError("L'")
    
    def remove_imp(self,impiegato,data)->None:
        if impiegato  in self.impiegati:
            self.impiegati.pop[impiegato] = data
        
        else:
            raise KeyError("L'Impiegato è già presente")
    
    def is_coin(self,impiegato)->bool:
        if impiegato in self.impiegati:
            return True
        
        else:
            return False
        
    def ult_imp(self,impiegato,data)->str:
        mass = date.min()
        jeff = None

        if not self.impiegati:
            raise ValueError("Vuoto")
        
        for impiegato,data in self.impiegati.items():
            if data >= mass:
                mass = data
                jeff = impiegato
        
        return jeff
