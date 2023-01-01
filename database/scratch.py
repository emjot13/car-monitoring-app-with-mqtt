import hashlib

plaintext = "hello".encode()
d = hashlib.sha256(plaintext)

# generate human readable hash of "hello" string
hash = d.hexdigest()
print(hash)

p = input()

pas = p.encode()
d1 = hashlib.sha256(pas)
hash1 = d1.hexdigest()

print(hash1 == hash)