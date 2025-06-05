def diffie_hellman(p, g, a, b):
    A = (g**a) % p
    B = (g**b) % p
    clave = (B**a) % p
    return clave

# Ejemplo
print(diffie_hellman(23, 5, 6, 15))