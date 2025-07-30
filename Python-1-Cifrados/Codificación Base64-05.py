import base64

def codificar_base64(texto):
    texto_bytes = texto.encode('utf-8')
    base64_bytes = base64.b64encode(texto_bytes)
    return base64_bytes.decode('utf-8')

# Ejemplo
print(codificar_base64("Hola Mundo"))
