PATH: str = 'Python/Lezione_15/example.txt'
mode: str = 'w'
encoding: str = 'utf-8'

file = open(PATH,mode)

print(file)
#input_text: str =input('Enter text to write to the file: ')
message: str = 'Hello, world!\n'
output: str = file.write(message)
print(message)
print(output)
file.close()

# file = open('Lezione_1/example.txt', 'a')
#try