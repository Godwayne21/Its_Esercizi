# 9-3. Users

class User:

    def __init__(self, first_name, last_name, age, gender)->None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):

        print(f"The name is {self.first_name}\nThe last name is {self.last_name}\nAge is: {self.age}\nThe gender is: {self.gender}")
    
    def greet_user(self):

        print (f"Hello {self.first_name} {self.last_name}!")
    
diego = User("Diego", "Laghetti", 19, "Gay")
luca = User("Luca", "Taggi", 36, "Lesbica")
claudio = User("Claudio", "Beni", 69, "Pansessuale")

diego.describe_user()
luca.describe_user()
claudio.describe_user()

diego.greet_user()
luca.greet_user()
claudio.greet_user()