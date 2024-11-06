import time
def dinput(text, delay=0.04):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay) 
    return input()
import time
def D(text, delay = 0.03):
    for letter in text:
        print(letter, end='',flush=True)
        time.sleep(delay)

D("Calculadora con una sola variable:\n")
while True:                   '''añadí un while True para que el programa pueda repetirse por una sentencia condicional, así me evito ejecutar otra vez lo mismo.'''
    D("\n********************\n")
    D("* MENÚ DE OPCIONES *")
    D("\n********************\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Exponente.")
    print("7. Módulo o resto.\n")
    ans1 = dinput("Introduce la opción deseada: ")
    ans = int(ans1)
    if ans == 1:
        D("\nElegiste Suma.\n")
        num1 = (int(input("Introduce el primer número: ")))
        num2 = (int(input("Introduce el segundo número: ")))
        resultado = num1 + num2
        print("\nEl resultado de la suma es:", resultado,"\n")
        
    elif ans == 2:
        D("Elegiste Resta.\n")
        num1 = (int(input("Introduce el primer número: ")))
        num2 = (int(input("Introduce el segundo número: ")))
        resultado = num1 - num2
        print("\nEl resultado de la resta es:", resultado,"\n")
      
    elif ans == 3:
        D("Elegiste Multiplicación.\n")
        num1 = (int(input("Introduce el primer número: ")))
        num2 = (int(input("Introduce el segundo número: ")))
        resultado = num1 * num2
        print("\nEl resultado de la multiplicación es:", resultado,"\n")
     
    elif ans == 4:
        D("Elegiste División.\n")
        num1 = (int(input("Introduce el primer número: ")))
        num2 = (int(input("Introduce el segundo número: ")))
        resultado = num1 / num2
        print("\nEl resultado de la división es:", resultado,"\n")
      
    elif ans == 5:
        D("Elegiste División entera.\n")
        num1 = (int(input("Introduce el primer número: ")))
        num2 = (int(input("Introduce el segundo número: ")))
        resultado = num1 // num2
        print("\nEl resultado de la división entera es:", resultado,"\n")

    elif ans == 6:
        D("Elegiste Exponente.\n")
        num1 = (int(input("Introduce el número: ")))
        num2 = (int(input("Introduce el exponente: ")))
        resultado = num1 ** num2
        print("\nEl resultado del exponente es:", resultado,"\n")

    elif ans == 7:
        D("Elegiste Módulo o resto.\n")
        num1 = (int(input("Introduce el número: ")))
        num2 = (int(input("Introduce el segundo número: ")))
        resultado = num1 % num2
        print("\nEl módulo es:", resultado,"\n")

    else:
        print("Opción no existente.")

    repetir = input("¿Quieres realizar otra operación? si/no: ").lower() #lower es para convertir toda respuesta a minúsculas, así puedes poner hasta "Si" o "sI" y se ejecutará.
    if repetir != 'si': #Aquí está la sentencia condicional, (!=) significa "Si es diferente a".
        print("Finalizando el programa.")
        break #El break es para, por si le puse algo diferente a "si" el while true ya no vuelve a ejecutarse.
#Espero te guste.
