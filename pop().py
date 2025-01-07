#Con este método, eliminamos cosas de la lista que nosotros queramos.


vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
print(f"Elemento eliminado: {vocales.pop()}")
print(f"Lista; {vocales}")

vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
print(f"Elemento eliminado en la posición 2: {vocales.pop(2)}")
print(f"Lista; {vocales}")

vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
print(f"Elemento eliminado en la posición 0: {vocales.pop(0)}")
print(f"Lista; {vocales}")

vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
print(f"Elemento eliminado en la posición 5: {vocales.pop(5)}") #<-- aquí estoy haciendo un error adrede, esto para ejemplificar que no se puede eliminar una posición no existente.
print(f"Lista; {vocales}")


