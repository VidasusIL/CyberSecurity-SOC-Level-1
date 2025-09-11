from Crypto.Util.number import inverse, long_to_bytes

p=4391
q=6659
e=65537
c=26600513

n = p * q

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c, d, n)

plaintext = long_to_bytes(m)
print("Decrypted message:", plaintext)
