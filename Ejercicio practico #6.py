frase = input("Introduce una frase: ")
palabra = input("Introduce una palabra a eliminar: ")

substring = ""

indice = frase.find(palabra)
substring = frase[0:indice] + frase[indice+len(palabra)+1:]

print(f"Cadena resultante: {substring}")