import numpy as np

def cifrar_hill(mensaje, matriz_clave):
    mensaje_vector = [ord(c) - ord('A') for c in mensaje.upper()]
    mensaje_cifrado = np.dot(mensaje_vector, matriz_clave) % 26
    return ''.join(chr(c + ord('A')) for c in mensaje_cifrado)

# Ejemplo
matriz_clave = np.array([[6, 24], [1, 13]])
print(cifrar_hill("HI", matriz_clave))
