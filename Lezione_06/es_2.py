class Student:

    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.myname = name
        self.course = studyProgram
        self.age = age
        self.gender = gender


    def printInfo(self):
        print(f"Name is {self.myname}, the course is {self.course}, the age is " )
        
godwayne = Student("Godwayne R.", "Cybersecurity")
claudio = Student("Claudio B.", "Cybersecurity")
alessio = Student("Alessio R.", "Cybersecurity")

godwayne.printInfo()
claudio.printInfo()
alessio.printInfo()
