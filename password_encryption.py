from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
import base64
import os

def encrypt_password(password, key):
    # Pad password to ensure it's a multiple of block size
    padder = padding.PKCS7(128).padder()
    padded_password = padder.update(password.encode()) + padder.finalize()

    # Encrypt password using AES
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_password = encryptor.update(padded_password) + encryptor.finalize()
    
    # Return encrypted password and iv (base64-encoded)
    return base64.b64encode(encrypted_password).decode(), base64.b64encode(iv).decode()

def decrypt_password(encrypted_password, iv, key):
    encrypted_password = base64.b64decode(encrypted_password)
    iv = base64.b64decode(iv)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_password = decryptor.update(encrypted_password) + decryptor.finalize()

    # Unpad the password
    unpadder = padding.PKCS7(128).unpadder()
    password = unpadder.update(padded_password) + unpadder.finalize()
    
    return password.decode()

# Generate a random key
key = os.urandom(32)  # AES-256 key
encrypted_password, iv = encrypt_password("my_secret_password", key)
print(f"Encrypted password: {encrypted_password}")

decrypted_password = decrypt_password(encrypted_password, iv, key)
print(f"Decrypted password: {decrypted_password}")
