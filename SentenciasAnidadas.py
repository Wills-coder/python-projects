#Para Delay con imput:
import time
def D(text, delay=0.03):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
    return input()

#Para Delay sin input, solo texto impreso en pantalla:
import time
def D1(text, delay=0.03):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)

print("=========")
print("Conversor")
print("=========\n")

D1("Menú de opciones: \n")
print()
D1("Presiona 1 para convertir de número a palabra.\n")
D1("Presiona 2 para convertir de palabra a número.\n")
print()

opcion = D("¿Cuál es tu opción deseada?: ")
print()
ans = int(opcion)
if ans == 1:
    D1("\n Conversor de número a palabra: \n")
    opcion1 = D("¿Cuál es el número que quieres convertir a palabra?: ")
    print()
    ans1 = int(opcion1)
    if ans1 == 1:
        D1("El número es 'UNO'.")
    elif ans1 == 2:                     #Esta es la S.C ANIDADA.
        D1("El número es 'DOS'.")
    elif ans1 == 3:
        D1("El número es 'TRES'.")
    elif ans1 == 4:                 
        D1("El número es 'CUATRO'.")
    elif ans1 == 5:
        D1("El número es 'CINCO'.")
    else:
        D1("El número aún no está registrado, aún...")

elif ans == 2:
    D1("\n Conversor de palabra a número: \n")
    ans2 = D("Cuál es la palabra que deseas convertir a número?: ")
    ans2 = ans2.lower()#Aquí hago que todo se convierta a minúscula, así puedes ingresar, por ejemplo "CuAtRo" e igual lo reconoce como cuatro.
    print()
    if ans2 == "uno":
        D1("El número es '1'.")
    elif ans2 == "dos":
        D1("El número es '2'.")
    elif ans2 == "tres":
        D1("El número es '3'.")
    elif ans2 == "cuatro":                 
        D1("El número es '4'.")
    elif ans2 == "cinco":
        D1("El número es '5'.")
    else:
        D1("El número aún no está registrado, aún...")
    
else:
    D1("Opción no disponible.")

#Solo por capricho, un nuevo tiempo para el "Fin." hahah
import time
def Fin(text, delay=0.70):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
print("\n") #ahora sé cómo utilizar "\n" así que ya no será tan molesto.
Fin("Fin.")
