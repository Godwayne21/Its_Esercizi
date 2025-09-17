from persona import Persona
from dottore import Dottore
from paziente import Paziente

class Fattura():

    def __init__(self,patient:list[Paziente], doctor: Dottore, fatture:int, salary:int)->None:
        if doctor.isAValidDoctor is True:
            self.fatture = len(patient)
            self.salary = salary

        else:
            print ("Non è possibile creare la classe fattura poichè il dottore non è valido!")
            self.patient = None
            self.dottore = None
            self.fatture = None
            self.salary= None
    
    def getSalary(self,dottore,patient)->float:
        self.salary = dottore.getParcel * len(self.patient)
        return self.salary
    
    def getFatture(self,patient)->int:
        self.patient = patient
        return self.patient
    
    def addPatient(self, newPatient, patient)->None:
        self.patient.append(newPatient)
        self.getSalary()
        self.getFatture()

        print (f"Alla lista del Dottor cognome è stato aggiunto il paziente {self.getidCode()}")
    
    def removePatient(self, idCode): 
        self.patient.remove(idCode)
        self.getFatture()
        self.getSalary()

        print(f"Alla lista del Dottor cognome è stato rimosso il paziente {self.getidCode()}")