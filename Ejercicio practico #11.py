Lista = ["A","B","b","c","E","E","f",]
print(f"lista original: {Lista}")
while True:
    delete = input("Introduce el elemento que deseas eliminar: ")

    for _ in Lista:
        if delete.lower() in Lista:
            Lista.remove(delete.lower())
        elif delete.upper() in Lista:
            Lista.remove(delete.upper())

    print(f"Elemento eliminado: {Lista}")