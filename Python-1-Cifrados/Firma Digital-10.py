from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def crear_firma(mensaje, clave_privada):
    hash = SHA256.new(mensaje.encode())
    firma = pkcs1_15.new(clave_privada).sign(hash)
    return firma

def verificar_firma(mensaje, firma, clave_publica):
    hash = SHA256.new(mensaje.encode())
    try:
        pkcs1_15.new(clave_publica).verify(hash, firma)
        return True
    except (ValueError, TypeError):
        return False

# Generar claves RSA
key = RSA.generate(2048)
clave_privada = key
clave_publica = key.publickey()

# Ejemplo
mensaje = "Hola Mundo"
firma = crear_firma(mensaje, clave_privada)
print(verificar_firma(mensaje, firma, clave_publica))