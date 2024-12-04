nombre = "GaBrIeL AgUaYO wIllS"
nombre = nombre.istitle()
print(nombre)

nombre = "GaBrIeL AgUaYO wIllS"
nombre = nombre.title()
print(nombre)

nombre = nombre.istitle()
print(nombre)

#Práctica interactiva
name = input("Ingresa tu nombre: ")
last = input("Ingresa tu apellido: ")
full = f"{name} {last}"
print()
print(f"¿Tu nombre está bien escrito?: {full.istitle()}")
print(f"Apliquemos el formato: {full.title()}")
print(f"Volvemos a imprimir el nombre: {full}")