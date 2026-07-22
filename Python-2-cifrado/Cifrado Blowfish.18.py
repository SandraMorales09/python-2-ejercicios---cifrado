from Crypto.Cipher import Blowfish

def cifrar_blowfish(texto, clave):
    cipher = Blowfish.new(clave.encode(), Blowfish.MODE_ECB)
    texto = texto.ljust(8, ' ')
    cifrado = cipher.encrypt(texto.encode())
    return cifrado

# Ejemplo
print(cifrar_blowfish("Hola", "clave123"))