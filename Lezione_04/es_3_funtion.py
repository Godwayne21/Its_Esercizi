def print_numbers(a):
    for i in a:
        print(i)
        
        
lenght_Of_List = (int(input('What is the length of your list?: ')))
list_numbers = [int(input('Insert a list of numbers')) for i in range(lenght_Of_List)]

print_numbers(list_numbers)