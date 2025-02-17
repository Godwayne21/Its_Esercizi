# esercizi (tipi di dato, operatori, collection)

#2-3

#name = input ('Enter your name: ')

#print (f"Hello {name}, would you like to learn some Python today?")

#2-4

#name = str(input ('Enter your name: '))

#print (name.lower())
#print (name.upper())
#print (name.title())

#2-5
#name = 'Socrate'

#quote = ('"Sapere di non sapere"')

#print (f"{name} once said, {quote}")

#2-6

#famous_person = 'Wayne'

#quote = ('"Chill"')

#print (f"{famous_person} once said, {quote}")

#3-1

#names = ['Pogs', 'Baks', 'Dons', 'Esi']

#print (names[0])
#print (names[1])
#print (names[2])
#print (names[3])

#3-2

#names = ['Pogs', 'Baks', 'Dons', 'Esi']

#print (f'Hello {names[0]}!')
#print (f'Ciao {names[1]}!')
#print (f'Hola {names[2]}!')
#print (f'Konichiwa {names[3]}!')

#3-3

#mode_of_transportation = ['Cafè Racer' , 'Muscle car', 'Jet']

#print (f'My favorite type of motorcycles are: {mode_of_transportation[0]}')
#print (f'I like {mode_of_transportation[2]} more than Sports Car')
#print (f'{mode_of_transportation[2]} are faster than:\n{mode_of_transportation[0]}\nor\n{mode_of_transportation[1]} ')

#3-4

#names = ['Pogs', 'Baks', 'Dons', 'Esi']
#for i in names:
#    print (f'{i}, I would like if you could come to my party!')
#for index in range(len(names)):
#    print (f'{names[index]}, I would like if you could come to my party!')

#3-5   
#names = ['Pogs', 'Baks', 'Dons', 'Esi']
    
#names[1] = 'Jem'

#for i in names:
#    print (f'{i}, I would like if you could come to my party!')

#3-6
#names = ['Pogs', 'Baks', 'Dons', 'Esi']

#names.insert(0,'Atat')
#names.insert(2,'Sam')
#names.append('Jem')

#for i in names:
#    print(f'{i}, I found a bigger table and invited more people to the party!')
    
#3-7    
#names = ['Pogs', 'Baks', 'Dons', 'Esi']

#names.insert(0,'Atat')
#names.insert(2,'Sam')
#names.append('Jem')

#print ('Sorry, I can invite only two people for dinner.')
#copia = names[:]
#for index in range(len(copia)):
    
#    removed = names.pop(0)
    
#    if (len(names)) == 2:
#        break
    
#print(names)

#while (len(names)) >= 3 :
    
#    uninvited = names.pop(0)
    
#    print(f"{uninvited} Sorry I can't invite you to dinner")
    
#for i in names:
    
#    print (f"Hello, {i}, you're still invited to my party!")
    

#print(names)
#del names[0] #'primo modo'
#del names[0]
#print(names)

#for index in range(len(names)):  #'secondo modo'
    
#    del names[0]
    
 #   if (len(names)) == 0:
        
#        break
#print (names)

#3-8

#places = ['Switzerland', 'Korea', 'Japan', 'Usa', 'Dubai']

#print(places)

#organized = sorted (places)

#print(organized)

#contrtario = sorted (organized, reverse=True)

#print(contrtario)

#places_1 = places

#places_1.reverse()

#print(places_1)

#places_1.reverse()

#print(places_1)

#places_1.sort()

#print(places_1)

#places_1.sort(reverse= True)

#print(places_1)

#3.9

#names = ['Pogs', 'Baks', 'Dons', 'Esi']

#names.insert(0,'Atat')
#names.insert(2,'Sam')
#names.append('Jem')

#print(f"I'm inviting {len(names)} in total")

#3.10 # da finire

#sports = ['Basketball', 'Soccer', 'Swimming', 'Baseball', 'Bowling',]

#da finire

#lista_vuota =[]

#print(lista_vuota)

#x = [input('add names of sports:')]

#lista_vuota = x

#print (lista_vuota)

#6.1

#persone = {'name': 'Sam','last_name': 'Tayag', 'age': 5, 'address': 'Rome'}

#for i in persone:
    
#    print (persone[i])
    
#6.2

#age = {'Nica': 24,'Dom': 23, 'Robby': 33, 'Chiara': 37, 'Ivan': 19}

#for key, value in age.items():
    
#    print (key, value)


#6.3

#glossary = {'Integer (int)': "Numbers without decimals. Can be positive or negative.",
#'Float (float)': "Numbers with decimals. Can be positive or negative.", 
#'String (str)': "Textual data, but really, can be any symbols as long as it’s in quotation marks",
#'Boolean (bool)': "Value that’s returned by logical operations. Can only be True or False",
#'Variable': "a name that references a value stored in the computer’s memory."}

#for key, value in glossary.items():
    
#    print(f' {key}:\n {value}')

#6.7

#person1 = {'name': 'Sam','last_name': 'Tayag', 'age': 5, 'address': 'Rome'}
#person2 = {'name': 'Atat','last_name': 'Tayag', 'age': 0, 'address': 'Rome'}
#person3 = {'name': 'Pogs','last_name': 'Tayag', 'age': 18, 'address': 'Rome'}

#people = [person1,person2,person3]

#for index in range(len(people)):
    
#    print (people[index])
    
#    print (f'{people[0]} \n{people[1]} \n{people[2]}')
    
#6.10
    
# = {'a':1,'b':2,'c':3,'d':4,'e':5}

#for i in num: 
    
#    num[i]=6,8,7
    
#    print(num)


#6.11

city = { 'Roma': 1, 'Milano': 2, 'Napoli': 3}

information = {'country': 'Italy', 'population': '1M', 'fact': 'pizza'}

#for key in city.items():#, information.items():
    
#    print(key)
    
#    for value in information.items():
        
#        print(value)




