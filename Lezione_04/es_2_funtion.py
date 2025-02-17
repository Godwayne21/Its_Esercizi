def check_length (a):
    
    if len(a) > 10:
        print (f' len of {a} is bigger than 10')
        
    elif len(a) < 10:
        print (f' len of {a} is smaller than 10')
        
    else:
        print (f'len of {a} is equal to 10')
        
check_length('Hello')