
from Crypto.Cipher import AES
import hashlib
import os

def cifrar_aes(texto, clave):
    key = hashlib.sha256(clave.encode()).digest()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(texto.encode())
    return nonce, ciphertext

# Ejemplo
nonce, ciphertext = cifrar_aes("Hola Mundo", "mi_clave")
print("Cifrado:", ciphertext)