def cifrar_xor(texto, clave):
    resultado = ''. join(chr(ord)(c) ^ clave) for c in texto)
        return resultado
mensaje = "Python Rocks"
clave = 42
mensaje_cifrado = cifrar_xor(mensaje_clave)
mensaje_descifrado = cifrar_xor(mensaje_cifrado, clave)

print("Mensaje cifrado:", mensaje_cifrado)
print("Mensaje descifrado", mensajes_descifrado)