from enum import StrEnum, auto
from typing import Any, Self
import re

class Indirizzo:
    def _init_(self, via: str, civico: str, cap: str) -> None:
        if not isinstance(via, str) or not isinstance(civico, str) or not (isinstance(cap, str) and len(cap) == 5 and cap.isdigit()):
            raise TypeError("Dati non validi per un indirizzo")
        self.via = via
        self.civico = civico
        self.cap = cap

    def get_via(self) -> str: return self.via
    def get_civico(self) -> str: return self.civico
    def get_cap(self) -> str: return self.cap

    def _hash_(self) -> int:
        return hash((self.via(), self.civico(), self.cap()))

    def _eq_(self, other: Any) -> bool:
        if other is None or not isinstance (other, type(self)) or hash(self) != hash(other):
            return False
        return (self.via(), self.civico(), self.cap()) == (other.via(), other.civico(), other.cap())

class Telefono:
    def _init_(self, numero: str) -> None:
        if numero != re('^\d{10}$'):
            raise TypeError("Dati non validi")
        
        self.numero = numero

    def get_numero(self) -> str:
        return self.numero

    def _hash_(self) -> int:
        return hash(self.numero())

    def _eq_(self, other: Any) -> bool:
        if other is None or not isinstance (other, type(self)) or hash(self) != hash(other):
            return False
        return self.numero() == other.numero()
    
class Stipendio:
    # tipo di dato Reale >= 0
    def _new_(cls, s: int|float|str|bool|Self) -> Self:
        #invoco il metodo new della suoerclasse; che è 'int'
        n: float = super()._new_(cls, s)

        if n >= 0:
            return n
        raise ValueError(f"il numero inserito {s} è negativo")
    
class Budget:
    def _new_(cls, b: int|float|str|bool|Self) -> Self:
        n: float = super()._new_(cls, b)
        if n >= 0:
            return n
        raise ValueError(f"il numero inserito {b} è negativo")
