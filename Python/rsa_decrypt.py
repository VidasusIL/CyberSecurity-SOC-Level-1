 import sys
from Crypto.Util.number import inverse, long_to_bytes

if len(sys.argv) != 5:
    print("Usage: python3 rsa_decrypt.py p q e c")
    sys.exit(1)

p = int(sys.argv[1])
q = int(sys.argv[2])
e = int(sys.argv[3])
c = int(sys.argv[4])

n = p * q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

m = pow(c, d, n)
print(long_to_bytes(m))


##end
