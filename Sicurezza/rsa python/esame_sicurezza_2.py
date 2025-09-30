#Es.1
# il messaggio originale è una parola di cinque lettere maiuscole e minuscole.

messaggio = 204751668535 # base 10

n = 514948966453 #modulo

e = 3 #esponente pubblico

x = False #serve per interrompere i cicli

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#ciclo per trovare le diverse combinzionni possibili
for p1 in alphabet:
    if x:
        break
    for p2 in alphabet:
        if x:
            break
        for p3 in alphabet:
            if x:
                break
            for p4 in alphabet:
                if x:
                    break
                for p5 in alphabet:
                
                    key = p1 + p2 + p3 + p4 + p5 #combinazione di lettere
                    
                    try:
                        key2 = int(key.encode('utf-8').hex(),16) #converto in intero
                        crypt = pow(key2,e,n)#simulo rsa

                        if crypt == messaggio: #verifico se messaggio cryptato è uguale alla parola trovato nel ciclo
                            print(f"Mesaggio = {key}")
                            x=True
                            break
                    
                    except:
                        continue



#Es. 2
'''Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
d = inverse(e, phi) dove ph = (p-1)*(q-1).

Sia dato n (pari a p*q) = 51151902024533551
e siano
e (esponente pubblico) = 3
C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
Decifrare il messaggio
NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata...'''

c = 51151902024533551 #modulo

fattori = []
divisore = 2
n = c

while divisore <= n :
    if n % divisore == 0:
        fattori.append(divisore)
        n //= divisore
    else:
        divisore += 1

p, q = fattori
phi = (p-1)*(q-1) #serve per trovade d

e_pub = 3

messaggio_cifrato = 10002041662569686 

d = pow (e_pub,-1,phi) #esponente privata trovata con l'inversa dell'algoritmo di euclide


mess_dec = pow(messaggio_cifrato,d,c) #decifro il messaggio

length = (mess_dec.bit_length() +7) // 8
mess_byte = mess_dec.to_bytes (length, 'big')
mess_dec_text = mess_byte.decode ('utf-8')

print (f'{messaggio_cifrato} = {mess_dec_text}')