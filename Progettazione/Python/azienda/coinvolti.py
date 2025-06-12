from custom_types import RealGEZ
from datetime import date
from impiegato import Impiegato
from progetto import Progetto
from typing import Any

class Coinvolti:

    _impiegato:Impiegato # immutabile e noto alla nascita
    _progetto:Progetto #immutabile e noto alla nascita
    _data : date # immutabile e noto alla nascita

    def __init__(self, i:Impiegato, p:Progetto, d:date)->None:
        self._impiegato:Impiegato = i
        self._progetto:Progetto = p
        self._data:date = d
    
    