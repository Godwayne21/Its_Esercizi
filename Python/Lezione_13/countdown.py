import time
'''
Write a Python function called countdown that takes a positive integer 
n as input and prints a countdown from n to zero.
If the input number is negative, display an error message.
To implement the function, you must exclusively use a while loop and the parameter 
n passed as input to the function.
Declaring any additional variables inside the function is not allowed.
Then, call the function with n = -5 and n = 5.
Expected Output:
Error! Inserted number is negative!
-------------------------------------------------
5
4
3
2
1
0
'''
#defiinsci la funzione
def countdown(n)->None:

#verificare se n > 0
    if n < 0:
        print("Errore!")
#ciclo while per stampare n fino a zero
    while n >= 0:

        time.sleep(1) # attende un tot di tempo prima di stampare

        print(n) # stampa n attuale

        n -= 1 # sottraggo 1 ad n

countdown(5)
countdown(-5)