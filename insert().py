#insert() es igual que append(), solo que nos solicita un número entero para determinar la posición del string que deseemos añadir. 

print("Lista original: ")
letters = ["b","d","f","g"]
print(f"Lista: {letters}")

print("\nInsertando 'a' en posición 0")
letters.insert(0, "a")
print(letters)

print("\nInsertando 'c' en posición 2")
letters.insert(2, "c")
print(letters)

print("\nInsertando 'e' en posición 4")
letters.insert(4, "e")
print(letters)

print("\nInsertando 'z' en posición 100")
letters.insert(100, "z")
print(letters)
