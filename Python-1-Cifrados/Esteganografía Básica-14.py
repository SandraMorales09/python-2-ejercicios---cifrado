from PIL import Image

def ocultar_mensaje(imagen, mensaje):
    img = Image.open(imagen)
    datos = img.getdata()
    mensaje_binario = ''.join(format(ord(c), '08b') for c in mensaje)
    datos_modificados = []

    for i, (r, g, b) in enumerate(datos):
        if i < len(mensaje_binario):
            r = (r & ~1) | int(mensaje_binario[i])
        datos_modificados.append((r, g, b))

    img_modificada = Image.new(img.mode, img.size)
    img_modificada.putdata(datos_modificados)
    img_modificada.save("imagen_modificada.png")

# Ejemplo
# ocultar_mensaje("imagen_original.png", "Hola")