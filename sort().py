#El método sort() nos permite acomodar los elementos de la mayor a menor, o mayor a menor.


"""Números:"""
print("De mayor a menor")
numeros = [5, 3, 1, 2, 4]
print(f"Sin el método sort(): {numeros}")
numeros.sort(reverse=True) #5, 4, 3, 2, 1.
print(f"Con el método sort(): {numeros}")

print("\nDe menor a mayor")
numeros = [5, 3, 1, 2, 4]
print(f"Sin el método sort(): {numeros}")
numeros.sort() #1, 2, 3, 4 , 5.
print(f"Con el método sort(): {numeros}")

"""Strings:"""
print("Strings, 'u' hasta 'a' ")
vocales = ["o","u","a","i","e",]
print(f"Sin el método sort(): {vocales}")
vocales.sort(reverse=True) #u, o, i, a, e.   
print(f"Con el método sort(): {vocales}")

print("Strings, 'a' hasta 'u' ")
vocales = ["o","u","a","i","e",]
print(f"Sin el método sort(): {vocales}")
vocales.sort(reverse=False) #a, e, i, o, u.
print(f"Con el método sort(): {vocales}")