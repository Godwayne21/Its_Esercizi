'''
Write a function called sum that takes a positive integer number n as input and 
returns the sum of the numbers from 0 to n.
If the input number n is negative, display an error message and the function must return None.
To implement the sum function, you must exclusively use a while loop and the parameter 
n passed as input to the function.
It is allowed to declare only one variable inside the function to manage the sum.
Then, call the function sum for n = -5 and n = 5.
Expected Output:
Error! Inserted number is negative!
None
--------------------------------------------------
15
'''

def sum(n:int)-> None:

    sum:int = 0
    # verificare se n è maggiore di 0
    if n < 0:
        print("Errore")
    
    # altri casi
    else:
        while n:

            sum += n

            n -= 1

        print(sum)
    return int(sum)

sum(5)
sum(-5)