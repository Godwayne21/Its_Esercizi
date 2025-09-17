from persona import Persona

class Paziente(Persona):

    __idCode__: str

    def __init__(self, idCode, first_name, last_name):
        super().__init__(first_name, last_name)

        self.__idCode__ = idCode
    
    def setIdCode (self, idCode)->None:
        self.__idCode__ = idCode
    
    def getidCode(self)->str:
        return self.__idCode__
    
    def patientInfo(self)->str:
        print(f"Paziente {self.__first_name__} {self.__last_name__}")
        print(f"ID: {self.__idCode__}")