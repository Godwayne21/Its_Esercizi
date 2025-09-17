from persona import Persona

class Dottore(Persona):

    __specialization__: str
    __parcel__: float

    def __init__(self, first_name, last_name, specialization, parcel)->None:
        super().__init__(first_name, last_name)

        if not isinstance (specialization, str):
            print ("La specializzazione non è una stringa!")
            self.__specialization__ = None
        else:
            self.__specialization__ = specialization

        
        if not isinstance (parcel, str):
            print ("La parcella inserita non è un float!")
            self.__parcel__ = None
        
        else:
            self.__parcel__ = parcel
        
    def setSpecialization(self,specialization)->None:
        if isinstance (specialization,str):
            self.__specialization__ = specialization
        
        else:
            print ("La specializzazione inserita non è una stringa!")

    def setParcel(self,parcel)->None:
        if isinstance(parcel,float):
            self.__parcel__ = parcel
        
        else:
            print("La parcella inserita non è un float!")
    
    def getSpecialization(self, specialization)->str:
        return self.__specialization__
    
    def getParcel(self, parcel)->float:
        return self.__parcel__

    def isAValidDoctor(self)->str:
        if self.__age__ > 30:
            print (f"Doctor {self.__first_name__} e {self.__last_name__} is valid!")
            return True
        
        else:
            print (f"Doctor {self.__first_name__} e {self.__last_name__} is not valid!")
            return False
    
    def doctorGreet(self)->str:
        self.greet() 
        print (f"Sono un medico {self.__specialization__}")