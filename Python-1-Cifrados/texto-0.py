from unittest import result


def cifrar_cesar(texto, clave):
    resultado =""
    for caracter in texto:
        if caracter.isalpha():
        desplazamiento = 65 if caracter.isupper() else 97
        resultado += chr(ord(caracter)- desplazamiento + clave) % 26 + desplazamiento)
    else:
        resultado += caracter
   return resultado # type: ignore

mensaje = input("Escribe el mensaje:")
clave = int(input("Escribe la clave"))
print("Mensaje cifrado:", cifrar_cesar(mensaje, clave))