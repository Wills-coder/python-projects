string = "Diana se peina sola"
rest = 0
start = "Ejemplos con startswith():"
end = "Ejemplos con endswith():"

print(f"\n{start.rjust(50, '=')}")

rest = string.startswith("D")
print(f"\n{string} comienza con la subcadena D: {rest}")

rest = string.startswith("d")
print(f"\n{string} comienza con la subcadena d: {rest}")

rest = string.startswith("Diana")
print(f"\n{string} comienza con la subcadena Diana: {rest}")

rest = string.startswith("se, 6")
print(f"\n{string} comienza con la subcadena se, desde la posición 6: {rest}")

rest = string.startswith("se, 6, 7")
print(f"\n{string} comienza con la subcadena se, desde la posición 6 hasta la posición 7: {rest}")

rest = string.startswith("se, 100, 100")
print(f"\n{string} comienza con la subcadena se, desde la posición 100 hasta la posición 100: {rest}")

rest = string.startswith("se, -4, -1")
print(f"\n{string} comienza con la subcadena se, desde la posición -4 hasta la posición -1: {rest}")


print(f"\n{end.rjust(50, '=')}")

rest = string.endswith("A")
print(f"\n{string} termina con la subcadena A: {rest}")

rest = string.endswith("a")
print(f"\n{string} termina con la subcadena a: {rest}")

rest = string.endswith("sola")
print(f"\n{string} termina con la subcadena sola: {rest}")

rest = string.endswith("sola, 10")
print(f"\n{string} termina con la subcadena sola: {rest}")

rest = string.endswith("s, 9, 14")
print(f"\n{string} termina con la subcadena s, desde la posición 9 hasta la posición 14: {rest}")

rest = string.endswith("s, 100, 100")
print(f"\n{string} termina con la subcadena s, desde la posición 100 hasta la posición 100: {rest}")

rest = string.endswith("s, -4, -2")
print(f"\n{string} termina con la subcadena s, desde la posición -4 hasta la posición -2: {rest}")

print("Fin")