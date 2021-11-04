from RSAlib import RSAObject

foo = RSAObject(700801,700849,65537)

M = 5479

c = foo.encrypt(M)
Md = foo.decrypt(c)

#print("Encrypted with N = %d and e = %d:\n" %(foo.N, foo.e))
print(foo.publicKey)
print(foo.privateKey)

print(c)
print(Md)