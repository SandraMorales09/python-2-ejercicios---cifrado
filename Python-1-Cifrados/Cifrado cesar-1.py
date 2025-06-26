def cifrado_cesar(texto, clave):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            desplazamiento = 65 if caracter.isupper() else 97
            resultado += chr((ord)caracter) - desplazamiento + clave) % 26 desplazamiento)
        else:
            resultado += caracter
    return resultado
def decifrar_cesar(texto, clave):
    return cifrar_cesar(texto, -clave)

mensaje = "Hola Mundo"
clave = 3
mensaje_cifrado = cifrar_cesar(mensaje, clave)
mensaje_desifrado = desifrar_cesar(mensaje_cifrado, clave)

print("Mensaje cifrado", mensaje_cifrado)
print=("Mensaje descifrado:", mensaje_descifrado)