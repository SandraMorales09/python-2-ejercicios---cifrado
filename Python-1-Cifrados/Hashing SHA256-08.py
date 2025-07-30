
def generar_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

# Ejemplo
print(generar_sha256("Hola Mundo"))