#Este método, remove(), nos permite eliminar un elemento de una lista, especificando lo que deseamos eliminar.

vocales = ["a","e","i","o","u"]
print(f"{vocales} \nElementos a eliminar: i")
vocales.remove("i")
print(vocales)

vocales = ["a","e","i","o","u"]
print(f"\n{vocales} \nElementos a eliminar: o")
vocales.remove("o")
print(vocales)

vocales = ["a","e","i","o","i"]
print(f"\n{vocales} \nElementos a eliminar: i") #Elimina solo la primera coincidencia.
vocales.remove("i")
print(vocales)

vocales = ["a","e","i","o","u"]
print(f"\n{vocales} \nElementos a eliminar: I") #Mayúscula #nos manda un error, ya que no hay qué eliminar.
vocales.remove("I")
print(vocales)