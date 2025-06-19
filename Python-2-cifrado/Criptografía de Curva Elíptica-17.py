from ecdsa import SigningKey, NIST384p

def curva_eliptica_firma(mensaje):
    clave_privada = SigningKey.generate(curve=NIST384p)
    firma = clave_privada.sign(mensaje.encode())
    clave_publica = clave_privada.get_verifying_key()
    return firma, clave_publica

# Ejemplo
firma, clave_publica = curva_eliptica_firma("Hola Mundo")
print(firma)