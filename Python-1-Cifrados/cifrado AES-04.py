from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def cifrar_aes(mensaje, clave):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv))
    encryptor = cipher.encryptor()
    texto_cifrado = encryptor.update(mensaje.encode()) + encryptor.finalize()
    return iv, texto_cifrado

def descifrar_aes(texto_cifrado, clave, iv):
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv))
    decryptor = cipher.decryptor()
    texto_descifrado = decryptor.update(texto_cifrado) + decryptor.finalize()
    return texto_descifrado.decode()

clave = os.urandom(32)
mensaje = "Hola AES!"
iv, mensaje_cifrado = cifrar_aes(mensaje, clave)
mensaje_descifrado = descifrar_aes(mensaje_cifrado, clave, iv)

print("Mensaje cifrado:", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)