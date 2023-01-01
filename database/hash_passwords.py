import hashlib

def hash_password(password):
    encoded_password = password.encode()
    hashed = hashlib.sha256(encoded_password)
    hashed = hashed.hexdigest()
    return hashed

