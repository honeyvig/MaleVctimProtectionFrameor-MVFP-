from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(key, data: bytes):
    return Fernet(key).encrypt(data)

def decrypt_data(key, token: bytes):
    return Fernet(key).decrypt(token)
