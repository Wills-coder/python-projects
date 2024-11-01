#Apuntes:
'''Operadores lógicos:

Operador:        Símbolo:

Conjunción         and <--- Aquí se deben cumplir ambas condiciones.
disyunción         or <--- Aquí se puede cumplir una, otra o ambas.
Negación           not <--- Aquí no hay una comparación, pero, por ejemplo:
                        -----------------------------------------------
                        |"if not num > 5: ((input: "2"))              |            
                        |        print("Se cumple, es menor que 5")"  |  
not:                    |"if not num > 5: ((input: "9"))              |
                        |       print("No se cumple, es mayor que 5")"|
                        -----------------------------------------------
                        '''
#Conjunción:
print("Conjunción (and): ")
num = float(input("Escribe un número mayor a 2 y menor a 5: "))
if num > 2 and num < 5:
    print("El número ", num, " cumple con la condición.\n")
else:
    print("El número", num, " NO cumple con la condición.\n")

#Disyunción
print("Disyunción (or): ")
word = input('Para cumplir con la condición, escribe "si" o "yes": ')
if word == "si" or word == "yes":
    print("La condición se ha cumplido.")
else:
    print("La condición NO se ha cumplido. ")

#Negación
print("\nNegación (not): ")
num = float(input('Introduce un número igual a 5: '))
if not num == 5:
    print("\n El número es diferente de 5 y sí cumple la condición (not).")
else:
    print("El número SÍ es igual a cinco y no se cumple la condición (not).")
  
print("\nFin.")
