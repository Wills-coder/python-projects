#estas practicas son muy cortas así que voy a hacer la 2 y la 3 de una sentada.
#Este es un diminuto ejercicio del profe.
#2: 

print("==================================================")
print("Programa que determina si un número es par o impar")
print("==================================================\n")

num = int(input("Por favor introduce un número entero: "))
if num % 2 == 0:
    print("El número",num,"es par.\n")
else:
    print("El número",num,"es impar.\n")

#Me había olvidado de como utilizar módulo pero ahora tengo toda la idea.

#3:
print("=====================================================================")
print("Programa para determinar cuál es el número más grande de tres números")
print("=====================================================================\n")
num1 = int(input("Ingresa el primer valor: "))
num2 = int(input("Ingresa el segundo valor: "))
num3 = int(input("Ingresa el tercer valor: "))

if num1 > num2 and num1 > num3:
    print("El número",num1,"es el número más grande de los tres.")
else:
    if num2 > num3:
        print("El número",num2,"es el número más grande de los tres.")
    else:
        print("El número",num3,"es el número más grande de los tres.")

print("Fin")
