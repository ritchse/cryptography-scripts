p = int(input("p: "))
q = int(input("q: "))
n = p*q
phi = (p-1)*(q-1)
print(f"φ(n): {phi}")
e = int(input("e: "))
d = pow(e,-1,phi)
print(f"d: {d}")
m = int(input("message (an int): "))
ciphered_m = pow(m,e,n)
print(f"E(m) = {ciphered_m}")
m2 = int(input("a message to decipher: "))
deciphered_m2 = pow(m2,d,n)
print(f"D(m) = {deciphered_m2}")