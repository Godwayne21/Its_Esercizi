import random
import time

quadrati:list = list(range(1,71))
t = 0
h = 0
vuota = '_'


def check_position(a,b) -> None:
    if a == b:
        print ('OUCH!!!')
    else:
        print (f"La tartaruga sta in quadrato {a} posizione {vuota}")
        print (f"La lepre sta in quadrato {b} posizione {vuota}")


#genera un numero casuale per la Tartaruga
def casuale_T(x: int) -> int:
    x = random.randint(1,10)
    return x

#genera un numero casuale per la Lepre
def casuale_H(y: int) -> int:
    y = random.randint(1,10)
    return y 


for i in quadrati:

    count = time.sleep(1)
#tartaruga
    if 1 <= casuale_T (i) <= 5:
        t += 3
        if t < 1:
             t== 1

    elif 6 <= casuale_T (i) <= 7:
        t -= 6
        if t < 1:
             t== 1
    
    elif 8 <= casuale_T (i) <= 10:
        t += 1
        if t < 1:
             t== 1
 
 #lepre   
    if 1 <= casuale_H (i) <= 5:
        h += 3
        if h < 1:
             h== 1

    elif 6 <= casuale_H (i) <= 7:
        h -= 6
        if h < 1:
             h== 1
    
    elif 8 <= casuale_H (i) <= 10:
        h += 1
        if h < 1:
             h== 1
    
    check_position(t,h)

    if t >= 70:
        print ("TORTOISE WINS! || VAY!!!")
        break
    
    elif h >= 70:
        print ("HARE WINS || YUCH!!!")
        break
    
    
    if count == 70 and t < 70 and h < 70:
        print ("IT'S A TIE.")
        count == 0