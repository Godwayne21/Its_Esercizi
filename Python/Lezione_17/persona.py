class Persona():
    __first_name__ : str
    __last_name__: str
    __age__: int

    def __init__(self, first_name,last_name)->None:
        if not isinstance (first_name, str):
            print("Il nome inserito non è una stringa!")
            self.__first_name__ = None
        
        if not isinstance (last_name, str):
            print("Il cognome inserito non è una stringa!")
            self.__last_name__ = None
        
        if isinstance(first_name and last_name,str):
            self.__age__ = 0

        else:
            self.__age__ = None
    
    def setName(self, first_name)->None:
        if isinstance(first_name,str):
            self.__first_name__ = first_name
        
        else:
            print("Il nome inserito non è una stringa!")
    
    def setLastName(self, last_name)->None:
        if isinstance(last_name,str):
            self.__last_name__ = last_name
        
        else:
            print("Il cognome inserito non è una stringa!")
    
    def setAge(self, age)->None:
        if isinstance(age,int):
            self.__age__ = age
        
        else:
            print ("L'età deve essere un numero intero!")
    
    def getName(self,first_name)-> str:
        return self.__first_name__
    
    def getLastName(self,last_name)-> str:
        return self.__last_name__
        
    def getAge(self,age)-> str:
        return self.__age__

    def greet (self)->str:
        print(f"Ciao, sono {self.__first_name__} {self.__last_name__}! Ho {self.__age__} anni!")