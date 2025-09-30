#modulo della chiave pubblica e privata 
n = '00e190f5b25958113fbfe01e464a0c'+\
    '84809e7761c18219f6ff68fe900961'+\
    '562a071eb2d7d3f2ea2a7987401da5'+\
    'dfb85396dbe3e73d528b800527fcdb'+\
    '62a22adda540f40913a0f0f6ce6937'+\
    '9ab61ea487af13f298e983153a4505'+\
    'f043fbd62260e86a7beae731e6cb44'+\
    '9374ad8c646dc4f15f31da89b6e01a'+\
    '4e8a2317fb1ef3eff40df08128f8cf'+\
    '411ef7bd5b254560da277c84c29c6f'+\
    'c690ce8e03aa011a83a85a86ceb9f9'+\
    '3069dc693e3341d7599978211428a6'+\
    'e46a4cdecf791453a44019b57fac35'+\
    '603c4d59163478cbc6fe131de3fdc2'+\
    '162ae98c174fc17992a2612df63627'+\
    'f7b63ca3c4aaa9259c80801ee0f953'+\
    '18c8839107ad80b218d8450e3c153e'+\
    '3711'

#esponente della chiave privata
e_pub = 3

#trasforma il modulo in numero intero
n_decimale = int(n,16)

print(f"n_decimale: {n_decimale}")

#messaggio da cifrare
messaggio = 'intel inside'

#trasforma stringa in numero esadecimale poi in intero
mess_int = int(messaggio.encode('utf-8').hex(),16)

print(mess_int)

#per cifrare il messaggio (messaggio intero ** esponente) * %n
mess_cifrato = pow(mess_int, e_pub, n_decimale)

print (mess_cifrato)

#come funzione pow()
#prova = (mess_int ** e)  % n_decimale

#esponente della chiave privata
es_priv =   '259828f30ee402dff550050bb70216' +\
            '156fbe904aeb0453d53c2a6d56e58e' +\
            '5c56851dcea35327071441355a464f' +\
            'f40dee79fb5134e3174000dbff79e5' +\
            'c5b1cf9b8ad356d89ad2d3cd118944' +\
            '73afc6169d2dfdc426eb2e3460d652' +\
            'b5ff4e5b1026bc69fc7bdda6773618' +\
            '93724210bcf6283a884f16f3d00462' +\
            '6c5b2ea9da7dfd53077a5eb169f66b' +\
            'b6a660ae8e7964bded2f71ba743113' +\
            '7465ef6eda94f7bb2d493590a9b097' +\
            '57ea3c9c6b25a9ba248352ba682fdc' +\
            'c06f51924616dd5787c7744e84377f' +\
            '90e178e420e4b1361599abea65705d' +\
            '5191d9887c9811b25c34480a31bdd2' +\
            '95804a106b2e2894bc63879728d61d' +\
            '2750114f10bc02ad31edcbcd0066ac' +\
            'd1'

#trasforma 
es_priv_int = int(es_priv, 16)

mess_dec = pow(mess_cifrato, es_priv_int, n_decimale)

print(mess_dec)

length = (mess_dec.bit_length() +7) // 8
mess_byte = mess_dec.to_bytes (length, 'big')
mess_dec_text = mess_byte.decode ('utf-8')

print (messaggio, mess_dec_text)