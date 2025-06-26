import hashlib

def verificar_integridad(archivo):
    hash_original = "abcdef1234567890"  # Hash esperado
    hash_archivo = hashlib.md5(open(archivo, 'rb').read()).hexdigest()
    return hash_archivo == hash_original

# Ejemplo
# print(verificar_integridad("mi_archivo.txt"))