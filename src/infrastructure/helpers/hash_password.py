import hashlib

def hash_sha265(password: str):
    encoded_string = password.encode('utf-8')
    hash_object = hashlib.sha256(encoded_string)
    hex_digest = hash_object.hexdigest()
    print(f"Original string: {password}")
    print(f"SHA-256 hash: {hex_digest}")
    return hex_digest
