def crack_hash_md5(hash_md5, lista_contraseñas):
    for contraseña in lista_contraseñas:
        if hashlib.md5(contraseña.encode()).hexdigest() == hash_md5:
            return contraseña
    return None

# Ejemplo
hash_md5 = hashlib.md5("secreto".encode()).hexdigest()
print(crack_hash_md5(hash_md5, ["1234", "secreto", "admin"]))