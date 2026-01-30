#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
#invertiamio il codice per decifrafe
# n, e e ct sono stati forniti
n = 984994081290620368062168960884976209711107645166770780785733
e = 0x10001
ct = 948553474947320504624302879933619818331484350431616834086273
# n will be 8 * (100 + 100) = 1600 bits strong (I think?) which is pretty good
#fattorizzo n 
p = 848445505077945374527983649411
q = 1160939713152385063689030212503

#calcolo rsa
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# si toglie perche sovvrascrive la flag prima che possa essere calcolato
'''FLAG = b"crypto{???????????????}"
pt = bytes_to_long(FLAG)'''

#non necessario perche devo solo decifrafe
'''print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")'''

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
#tolgo perchè fa il controllo solo se decrypted e e Flag dsono uguali durante la cifratura
#assert decrypted == FLAG

print (decrypted)