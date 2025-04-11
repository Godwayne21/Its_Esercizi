import time
# ricorsioni countdown

def countdown(n:int)->None:
    #n negative
    if n < 0:
        print("Error the number most be positive")
  
    # function stops when n = 0
    elif n == 0:
        print(0)
    
    # other cases
    else:

        print(n)
        time.sleep(1)
        countdown(n-1)

countdown(5)
countdown(-5)
countdown(0)