#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

e = 0x10001

p = getPrime(800)
q = getPrime(800)
n = p * q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# Messaggio
FLAG = b"crypto{???????????????}"
pt = bytes_to_long(FLAG)

# Cifratura
ct = pow(pt, e, n)


print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")


pt = pow(ct, d, n)

# Convertiamo il numero di nuovo in stringa (bytes)
decrypted = long_to_bytes(pt)

assert decrypted == FLAG

print (FLAG)