def cronometro(fun):
    def wrapper():

        import time
        start = time.time() #serve a chiedere che ore sono ora
        fun()
        print (time.time() - start) #sottraggo il tempo di adesso meno il tempo iniziale
    
    return wrapper

def prova2():
    print ("hello")

def prova():
    print ("ciao")

prova = cronometro(prova) #parametro fun di cronometro = prova

prova2 = cronometro(prova2)

print(prova) #location di memoria 

prova()
prova2()