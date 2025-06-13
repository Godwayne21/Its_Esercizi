from enum import *
from typing import Any
from datetime import date,datetime

class Impiegato:

    def __init__(self, nome:str, cognome:str, nascita: date, stipendio:float)->None:

        self.nome = nome
        self.cognome = cognome
        self.nascita = nascita
        self.stipendio = stipendio

    def get_nome (self, name:str)->str:
        return self.nome
    
    def get_cognome (self, cognome:str)->str:
        return self.cognome
    
    def get_nascita (self, nascita:date)->date:
        return self.nascita
    
    def get_stipendio (self, stipendio:float)->str:
        return self.stipendio