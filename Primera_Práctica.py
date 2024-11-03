#Este es un ejercicio práctico, tomando en cuenta absolutamente todo lo que he aprendido hasta ahora.
#Veremos Datos desde teclado, y sobre todo, muchas sentencias condicionales.
#He aquí la solicitud de trabajo práctico:

'''Una compañía solicita un sistema que determine los dias de vacaciones a los que tiene derecho un
trabajador, tomando en cuenta las siguientes características:

° Existen tres departamentos dentro de la compañia con sus respectivas claves:
1.- Dpto de atención al cliente. (clave 1)
2.- Dpto de logística. (clave 2)
3.- Gerencia. (clave 3)

Clave 1:                Clave 2:                Clave 3:
1 año: 6 días.          1 año: 7 días.          1 año: 10 días.              
2 a 6 años: 14 días.    2 a 6 años: 15 días.    2 a 6 años: 20 días.
7 años o +: 20 días.    7 años o +: 22 días.    7 años o +: 30 días:    '''
 #Bien, Empecemos:

import time
def DInput(texto, Retraso=0.03):
    for letra in texto:
        print(letra, end='',flush=True)
        time.sleep(Retraso)
    return input()
def D(text, delay=0.04):
    for letter in text:
        print(letter, end='',flush=True)
        time.sleep(delay)

print("=================================")
print("Sistema de consulta de vacaciones")
print("=================================\n")

D("\nHola, estimado trabajador.\n")
D("Para empezar, ¿Cuál es su nombre?\n")
name = DInput("Ingrese su nombre: ")
D("¡Hola "+name+ "! Empecemos por con su consulta.\n")
D("¿Cuál es su número de clave?\n")
key1 = DInput("Ingrese su número de clave: ")
key = int(key1)

if key == 1:
    print("\nDepartamento de atención al cliente.\n")
    D("Estimado trabajador, para calcular su derecho a vacaciones debemos saber su estadía.\n")
    D("A continuación, le daré las opciones a elegir para conocer sobre su tiempo de trabajo:\n")
    D("1.- 1 año\n")
    D("2.- 2 a 6 años\n")
    D("3.- Desde los 7 años o más\n")
    ans = DInput("Ingrese su selección: ")
    ans1 = int(ans)
    if ans1 == 1:
        D(name + ", usted tiene 6 días de vacaciones.\n")
    elif ans1 == 2:
        D(name + ", usted tiene 14 días de vacaciones.\n")
    elif ans1 == 3:
        D(name+ ", usted tiene 20 días de vacaciones.\n")
    else:
        D("Opción no existente.\n")
    D("\nFin.")


elif key ==2:
    print("\nDepartamento de logística.\n")
    D("Estimado trabajador, para calcular su derecho a vacaciones debemos saber su estadía.\n")
    D("A continuación, le daré las opciones a elegir para conocer sobre su tiempo de trabajo:\n")
    D("1.- 1 año\n")
    D("2.- 2 a 6 años\n")
    D("3.- Desde los 7 años o más\n")
    ans = DInput("Ingrese su selección: ")
    ans1 = int(ans)
    if ans1 == 1:
        D(name + ", usted tiene 7 días de vacaciones.\n")
    elif ans1 == 2:
        D(name + ", usted tiene 15 días de vacaciones.\n")
    elif ans1 == 3:
        D(name+ ", usted tiene 22 días de vacaciones.\n")
    else:
        D("Opción no existente.\n")
    D("\nFin.")

elif key==3:
    print("\nGerencia.\n")
    D("Estimado trabajador, para calcular su derecho a vacaciones debemos saber su estadía.\n")
    D("A continuación, le daré las opciones a elegir para conocer sobre su tiempo de trabajo:\n")
    D("1.- 1 año\n")
    D("2.- 2 a 6 años\n")
    D("3.- Desde los 7 años o más\n")
    ans = DInput("Ingrese su selección: ")
    ans1 = int(ans)
    if ans1 == 1:
        D(name + ", usted tiene 10 días de vacaciones.\n")
    elif ans1 == 2:
        D(name + ", usted tiene 20 días de vacaciones.\n")
    elif ans1 == 3:
        D(name+ ", usted tiene 30 días de vacaciones.\n")
    else:
        D("Opción no existente.\n")
    D("\nFin.")
    
else:
    D("Clave no existente.")

#Psdt:
#Lo hice a mi manera, ya que esto es un ejercicio práctico.

#El profe lo hizo de una manera distinta, si quieres, puedes ver el video para comprobar.

#https://www.youtube.com/watch?v=r4zmpyPaEzw&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=17
