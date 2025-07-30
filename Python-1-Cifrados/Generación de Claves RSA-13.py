from Crypto.PublicKey import RSA

def generar_claves_rsa():
    key = RSA.generate(2048)
    clave_privada = key.export_key()
    clave_publica = key.publickey().export_key()
    return clave_privada, clave_publica

# Ejemplo
clave_privada, clave_publica = generar_claves_rsa()
print(clave_privada)
print(clave_publica)