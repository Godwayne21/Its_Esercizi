class Animal:
    def __init__(self, name, type, habitat, legs):
        self.name = name
        self.type = type
        self.habitat = habitat
        self.legs = legs
    
    def showName(self):
        print(f"The name is: {self.name}")
    
    def setLegs(self):
        self.legs += 14
    
    def getLegs(self):
        print(f"{self.name} has {self.legs} legs")
    
    def printInfo(self):
        print(f"{self.name} is a {self.type} and it's habita is {self.habitat} and it ha {self.legs} legs")


cane = Animal("Bob", "Mammifero", "Terra", 4)
pesce = Animal("Piplup", "Anfibio", "Acqua", 0)
aquila = Animal("Winston", "Uccello", "Aria", 2)

cane.showName()
pesce.showName()
aquila.showName()

cane.setLegs()
pesce.setLegs()
aquila.setLegs()

cane.getLegs()
pesce.getLegs()
aquila.getLegs()

cane.printInfo()
pesce.printInfo()
aquila.printInfo()