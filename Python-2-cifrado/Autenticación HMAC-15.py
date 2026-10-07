import hmac
import hashlib

def autenticar_hmac(clave, mensaje):
    return hmac.new(clave.encode(), mensaje.encode(), hashlib.sha256).hexdigest()

# Ejemplo
print(autenticar_hmac("clave_secreta", "Hola Mundo"))
