import hashlib

def generar_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

# Ejemplo
print(generar_md5("Hola Mundo"))