from Crypto.Cipher import AES
import hashlib
import os

def encriptar_archivo(archivo, clave):
    key = hashlib.sha256(clave.encode()).digest()
    cipher = AES.new(key, AES.MODE_EAX)
    with open(archivo, 'rb') as f:
        datos = f.read()
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(datos)
    with open("archivo_encriptado", 'wb') as f:
        f.write(nonce + ciphertext)

# Ejemplo
# encriptar_archivo("mi_archivo.txt", "clave_secreta")