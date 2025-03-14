class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(f"Bob's age is {bob.age}")

if alice.age > bob.age:
    print("Alice's older than Bob")

else:
    print("Bob is older than Alice")

james = Person("James L.", 62)
dwight = Person("Dwight G.", 80)
sasha = Person("Sasha S.", 24)

people = [alice,bob,james,dwight,sasha]

youngest = people [0]
for i in people:

    if i.age < youngest.age:

        youngest = i

print(f"The youngest is {youngest.name}")