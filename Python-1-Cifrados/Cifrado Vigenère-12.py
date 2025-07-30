def cifrar_vigenere(texto, clave):
    resultado = ""
    clave = clave.upper()
    i = 0
    for char in texto:
        if char.isalpha():
            desplazamiento = ord(clave[i % len(clave)]) - ord('A')
            if char.islower():
                nuevo_char = chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
            else:
                nuevo_char = chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
            resultado += nuevo_char
            i += 1
        else:
            resultado += char
    return resultado

# Ejemplo
print(cifrar_vigenere("Hola Mundo", "clave"))