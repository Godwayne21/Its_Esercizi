def check_each(a):
    
    for i in a:
        
        if i > 5:
            print (f'{i} is bigger than 5')
            
        elif i < 5:
            print (f'{i} is smaller than 5')
            
        else:
            print (f'{i} is equal to 5')
            

lenght_Of_List = (int(input('What is the length of your list?: ')))
list_numbers = [int(input('Insert a list of numbers')) for i in range(lenght_Of_List)]

check_each(list_numbers)