from enum import *
from typing import Any
import re

class Indirizzo:

    def __init__(self, via:str, civico:str, cap:str)->None:
        if not isinstance(via, str) or not isinstance(civico, str) or not (isinstance(cap,str) and len(cap) ==5 and cap.isdigit()):
            raise TypeError("Dati non validi")
        self.via = via
        self.civico = civico
        self.cap = cap
    
    def via(self)->str:
        return self.via
    
    def civico(self)->str:
        return self.civico

    def __hash__(self)->int:
        return hash((self.via(), self.civico(), self.cap()))
    
    def __eq__(self, other:Any)->bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.via(), self.civico() ) == (other.via(), other.civico(), other.cap())

class Telefono:
    def __init__(self,numero:str)->None:
        if numero != re('^\d{10}$'):
            raise TypeError("Dati non validi")
        self.numero = numero
    
    def get_numero(self)->str:
        return self.numero
    
    def __hash__(self)->int:
        return self.numero
    
    def __eq__(self, other:Any)->bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.numero()) == (other.numero())

class Stipendio:
    def __init__(self,stipendio:float)->None:
        if stipendio < 0:
            raise TypeError("Dati non validi")
        self.stipendio =stipendio

    def get_stipendio(self)->float:
        return self.stipendio
    
    def __hash__(self)->int:
        return self.stipendio
    
    def __eq__(self, other:Any)->bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.stipendio()) == (other.stipendio())

class Budget:
    def __init__(self,budget:float)->None:
        if budget < 0:
            raise TypeError("Dati non validi")
        self.budget = budget

    def get_stipendio(self)->float:
        return self.budget
    
    def __hash__(self)->int:
        return self.budget
    
    def __eq__(self, other:Any)->bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.budget()) == (other.budget())