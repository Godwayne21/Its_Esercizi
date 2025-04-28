class Persona:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.age= 0
    
#funzione della classe persona che visualizza in output i dati di una persona
    def displayData(self)->None:
        print(f"Nome: {self.name}\nCognome: {self.last_name}\nEtà: {self.age}")

#funzione che consente di impostare il valore di self.name
    def setName(self, name:str)->None:
        self.name = name

#funzione che consente di impostare il valore di self.last_name
    def setLastName(self, last_name:str)->None:
        self.last_name = last_name

#funzione che consente di impostare il valore di self.last_name
    def setAge(self, age:int)->None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

#funzione che mi restituisce il valore di self.name
    def getName(self)->str:
        return self.name

#funzione che mi restituisce il valore di self.last_name
    def getLastName(self)->str:
        return self.last_name

#funzione che mi restituisce il valore di self.name
    def getAge(self)->int:
        return self.age

#metodo spea() per la classe Persona che consente di simulare un saluto
    def speak(self)->None:
        print(f"\nHello! my name is {self.getName()}!")