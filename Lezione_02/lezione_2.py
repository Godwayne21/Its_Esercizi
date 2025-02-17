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
names = ['Pogs', 'Baks', 'Dons', 'Esi']

names.insert(0,'Atat')
names.insert(2,'Sam')
names.append('Jem')

#print ('Sorry, I can invite only two people for dinner.')
#copia = names[:]
#for index in range(len(copia)):
    
#    removed = names.pop(0)
    
#    if (len(names)) == 2:
#        break
    
#print(names)

while (len(names)) >= 3 :
    
    uninvited = names.pop()
    
    print(f'{uninvited[]} Sorry I cant invite you to dinner')
    
print(names)
