from film import Film

class Azione(Film):

    __genere__:str = "Azione"
    __penale__:float = 3

    def __init__(self, id, title, genere:str, penale:float)->None:
        super().__init__(id, title)

        self.__genere__ = genere
        self.__penale__ = penale
    
    def setGenere (self)->str:
        return self.__genere__
    
    def setPenale (self)->float:
        return self.__penale__
    
    def calcolaPenaleRitardo(self, giorni)->float:
        return self.__penale__ * giorni

class Commedia(Film):

    __genere__:str = "Commedia"
    __penale__:float = 2.5

    def __init__(self, id, title, genere:str, penale:float)->None:
        super().__init__(id, title)
    
        self.__genere__ = genere
        self.__penale__ = penale
    
    def setGenere (self)->str:
        return self.__genere__
    
    def setPenale (self)->float:
        return self.__penale__
    
    def calcolaPenaleRitardo(self, giorni)->float:
        return self.__penale__ * giorni
    
class Drama(Film):

    __genere__:str = "Drama"
    __penale__:float = 2

    def __init__(self, id, title, genere:str, penale:float)->None:
        super().__init__(id, title)

        self.__genere__ = genere
        self.__penale__ = penale
    
    def setGenere (self)->str:
        return self.__genere__
    
    def setPenale (self)->float:
        return self.__penale__
    
    def calcolaPenaleRitardo(self, giorni)->float:
        return self.__penale__ * giorni