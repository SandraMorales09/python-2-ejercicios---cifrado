import hashlib
def generar_hash(texto):
    sha256_hash = hashlib.sha256(texto.encode()).hexdigest()
    return hash
mensaje = "Este es un mensaje importante"
hash_generando = generar_hash(mensaje)

print("Mensaje:", mensaje)
print("Hash SHA256:", hash_generado)