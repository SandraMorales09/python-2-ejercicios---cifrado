from Crypto.Cipher import ARC4

def cifrar_rc4(texto, clave):
    cipher = ARC4.new(clave.encode())
    cifrado = cipher.encrypt(texto.encode())
    return cifrado

# Ejemplo
print(cifrar_rc4("Hola Mundo", "clave123"))