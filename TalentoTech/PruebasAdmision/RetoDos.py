def cifrado_cesar(texto, desplazamiento):
    """
    Realiza el cifrado César en un texto dado.

    Args:
        texto (str): El texto a cifrar.
        desplazamiento (int): El número de posiciones a desplazar en el alfabeto.

    Returns:
        str: El texto cifrado.
    """
    resultado = ""
    for letra in texto:
        if letra.isalpha():  # Solo cifra letras (ignora espacios, números, etc.)
            base = ord('a') if letra.islower() else ord('A')
            indice = (ord(letra) - base + desplazamiento) % 26
            nueva_letra = chr(base + indice)
            resultado += nueva_letra
        else:
            resultado += letra  # Mantén caracteres no alfabéticos sin cambios
    return resultado

texto_original = input()
clave = int(input())
texto_cifrado = cifrado_cesar(texto_original,clave)

print(texto_cifrado)