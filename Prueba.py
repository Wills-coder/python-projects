#Hola bro, vas a disculpar el montón de "Print()'s" es que no sé cuál es la otra manera para hacer cambios de línea XD.
#Si tienes tiempo intenta resolver los ejercicios, si no, le pones cualquier cosa, igual le puse un else.

import time
def D(text, delay=0.30):
    for letter in text:
        print(letter, end='', flush=True) #Para que se vea bonito y no aparezca de la nada el txt.
        time.sleep(delay) #Me ayudé con Chatgpt, pero ahora lo tengo en la cabeza muahahahaaa.
    return input()

text0 = ("Prueba de matemáticas, 3er trimestre.")
text1 = (' Aprete "Enter" para continuar.')

D(text0 + text1)
print()


name = D("Nombre del estudiante: ")
D("Curso: ")
D("Fecha: ")
D("Carnet de identidad: ")

import time
def D1(text, delay=0.070):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)

D1(f'¡Hola, {name}! Fuiste exitosamente registrado a la prueba. ')
print() #Perdón por el dolor de ojos por estos prints hahaha
print()
D("Iniciemos por la primera pregunta: ")
print()
print()
D1("Una bicicleta tiene un precio de 1350Bs, y por su compra al contado tiene un descuento del 15%. ¿Cuánto debo pagar si la compro al contado? ")
print()
D1("Respuestas: (Responde en cantidad numérica por favor.)") 
print()
resp = D1("a) 1419.50")
print()
resp1 = D1("b) 6343.84")
print()
resp2 = D1("c) 1147.5")
print()
respuesta = D("Respuesta: ")
ans = float(respuesta)

if ans == 1147.5:
    D1("Respuesta Correcta.")
elif ans == 6343.84:
    D1("De dónde sacaste ese resultado oye? fuera de foco :v.")
elif ans == 1147.5:
    D1("tarau.")
else:
    D1("Respuesta incorrecta, flojonazo, no quisiste resolverlo ;'v")
print() #<-------Gracias a Dios no ves estos en la terminal.
print()
D(" Segunda pregunta: ")
print()
print()
D1("Un comerciante compra televisores a un costo de 3250Bs cada uno, y al venderlo debe ganar el 25% de lo invertido. ¿Cuánto será el valor final del televisor? ")
print()
D1("Respuestas: ") 
print()
resp = D1("a) 4062.5")
print()
resp1 = D1("b) 6343.74")
print()
resp2 = D1("c) 1656.5")
print()
respuesta1 = D("Respuesta: ")
ans = float(respuesta1)

if ans == 1147.5:
    D1("Respuesta Correcta. Sos un master, XD")
elif ans == 6343.74:
    D1("De dónde sacaste ese resultado oye? fuera de foco :v.")
elif ans == 1656.5:
    D1("tarau.")
else:
    D1("Respuesta incorrecta, tas aplazau.")
print()
print()
D1("Fin de la prueba, si aprobaste, sos un ídolo. Bv")

#Sé que esto es muy básico pero prometo mejorar, mañana haré inclusive un proyecto más grande, y quizás más interactivo.
"""Y soy consciente de que capaz y me compliqué con varias cosas, pues estuve toda la tarde con esto,
ya sabes, prueba y error, prueba y error, para que al final, literalmente lo más lógico y sencillo resultó ser la respuesta."""

#thx, I promise to improve every day.
