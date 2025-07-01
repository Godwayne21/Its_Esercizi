class Documento:

    _testo:str #memorizza qualsiasi contenuto testuale per il documento 

    def __init__(self,testo:str):
        self._testo = testo

    def getText(self)->str:
        return self._testo
    
    def setText(self,_testo)->None:
        