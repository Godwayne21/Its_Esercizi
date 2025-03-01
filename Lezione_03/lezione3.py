# Lezione 3

#4.1

#pizza = ['boscaiola', 'diavola', 'margherita']

#for i in pizza:
    
#    print (f'I like eating {i} pizza')
    
#print(' I really love pizza!')

#4.2

#animals = ['dogs', 'cats', 'giraffe']
 
#for i in animals:
    
#    print (f'{animals[0]} are very friendly \n{animals[1]} are very sensitive \n{animals[2]} have very long necks')
    
#    break

#for index in range(len(animals)):
    
#    print (f'{animals[index]} have for legs')

#4.3
#import time

#for numbers in range (1,21):
#     print (numbers)
     
#     time.sleep(0.5)
    
#4.4
#import time

#for millione in range (1000000):
    
#    print(millione)

#    time.sleep(1)
    
#4.5

#millione = list(range(1,1000001))

#print (min(millione))
#print (max(millione))
#print (sum(millione))

#4.6

#odd = list(range(1,20,2))

#for i in odd:
    
#    print (f'{i}')

#4.7

#multiplier_3 = list (range(3,30,3))

#for i in multiplier_3:
    
#    print (f'{i}')

#4.8

#cube = list(range(1,11))

#for i in cube:
    
#    print(f'{i**3}')

#4.9

#cube = [x**3 for x in range (10)]

#print (cube)

#4.10


#4.11

#pizza = ['boscaiola', 'diavola', 'margherita']
#pizza_friend = ['bianca', 'patate', 'formaggio']

#for i in pizza:
    
#    print(f' My favorite pizzas are: {pizza}')
    
#    break

#for i in pizza_friend:
    
#    print(f' My friend’s favorite pizzas are: {pizza_friend}')
    
#    break


#5.1
'''
car = "mustang"
motor = "harley"
boat = "yacth"
sport = "basketball"
shoes = "way of wade"

print("Is car == 'mustang'? I predict True.")
print(car == 'mustang')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs motor == 'harley'? I predict True.")
print(motor == 'harley')
print("\nIs motor == 'yamaha'? I predict False.")
print(motor == 'yamaha')

print("\nIs boat == 'yacth'? I predict True.")
print(boat == 'yacth')
print("\nIs boat == 'kayak'? I predict False.")
print(boat == 'kayak')

print("\nIs sport == 'basketball'? I predict True.")
print(sport == 'basketball')
print("\nIs sport == 'soccer'? I predict False.")
print(sport == 'soccer')

print("\nIs shoes == 'way of wade'? I predict True.")
print(shoes == 'way of wade')
print("\nIs shoes == 'lebron'? I predict False.")
print(shoes == 'lebron')
'''

# 5.2
'''
print ("computer" == "computer")
print ("computer" == "charger")

print ("Computer".lower() == "computer")
print ("Computer".lower() == "COMPUTER")

print ( 10 == 10)
print ( 10 == 5)
print ( 10 < 5)
print ( 10 > 5)
print ( 10 <= 5)
print ( 10 >= 5)

print ( 10 == 10 and 10 > 5)
print ( 10 == 10 and 10 < 5)
print ( 10 == 10 or 10 > 5)
print ( 10 == 10 or 10 < 5)

transport = ["car", "train", "boat"]

print ("car" in transport)
print ("bike" in transport)
'''

# 5.3
'''
alien_color = "green"

if alien_color == "green":
    print ("you just earned 5 points")

if alien_color == "red":
    None
'''

# 5.4
'''
alien_color = "green"

if alien_color == "green":
    print ("you just earned 5 points for shooting the alien")
else:
    print ("you just earned 10 points")

alien_color = "red"

if alien_color == "green":
    print ("you just earned 5 points for shooting the alien")
else:
    print ("you just earned 10 points")
'''

#5.5
'''
alien_color = "green"

if alien_color == "green":
    print ("you just earned 5 points")
elif alien_color == "red":
    print ("you just earned 10 points")
else:
    print ("you just earned 15 points")

alien_color = "yellow"

if alien_color == "green":
    print ("you just earned 5 points")
elif alien_color == "yellow":
    print ("you just earned 10 points")
else:
    print ("you just earned 15 points")

alien_color = "red"

if alien_color == "green":
    print ("you just earned 5 points")
elif alien_color == "yellow":
    print ("you just earned 10 points")
else:
    print ("you just earned 15 points")
'''

#5.6
'''
age = int(input("What's your age? "))

if age < 2:
    print ("You're a baby!")

elif age >= 2 & age < 4:
    print ("You're a toddler!")

elif age >= 4 & age < 13:
    print ("You're a kid!")

elif age >= 13 & age < 20:
    print ("You're a teenager!")

elif age >= 20 & age < 65:
    print ("You're a adult!")

else:
    print ("You're an aelder!")
'''

#5.7
'''
fruits = ['banana', 'apple', 'grapes', 'mango', 'pomelo']
favorite_fruits = ['banana', 'grapes', 'mango',]

if "banana" in favorite_fruits:
    print ("I really like Bananas!")

if "apples" in favorite_fruits:
    print ("I really like Apples!")

if "grapes" in favorite_fruits:
    print ("I really like Grapes!")

if "mango" in favorite_fruits:
    print ("I really like Mango!")

if "pomelo" in favorite_fruits:
    print ("I really like Pomelo!")
'''

#5.8
'''
names = ['James', 'Steph', 'Kyrie', 'John', 'Admin']

for i in names:
    if i == "Admin":
        print ("Hello Admin, would you like to see a status report?")
    
    else:
        print (f"Hello {i}, thank you for logging in again.")
'''

#5.9
'''
names = ['James', 'Steph', 'Kyrie', 'John', 'Admin']

names.clear()

if len(names) == 0:
    print("We need to find some users!")
'''

# 5.10
'''
current_users = ['James', 'Steph', 'Kyrie', 'John', 'Kevin']
new_users = ['James', 'Leo', 'Bob', 'John', 'Ed']

current_users_lower = [a.lower() for a in current_users]

for i in new_users:

    if i.lower() in current_users_lower:

        print(input(f"The name {i} is already taken. Insert a new name: "))
    
    else:
        print("Name is available")
'''

# 5-11

numbers = [range(1,10)]

for i in numbers:

    if i == 1:
        print(f"{i}st")
    
    elif i == 2:
        print(f"\n{i}nd")
    elif i == 3:
        print(f"\n{i}rd")
    else:
        print(f"\n{i}th")