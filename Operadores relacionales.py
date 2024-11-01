#https://www.youtube.com/watch?v=4vKrYztae2I&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=15: Este es el video del profe.

import time
def D(texto, retraso=0.03):
    for letra in texto:
        print(letra, end='',flush=True)
        time.sleep(retraso)
    return input()
import time
def D1(texto, retraso=0.03):
    for letra in texto:
        print(letra, end='',flush=True)
        time.sleep(retraso)

D1("\nIntroduce dos números a comparar: \n")
num0=D("\nIntroduce el primer número: ")
float(num0)
num1=D("Introduce el segundo número: ")
float(num1)
print("\nLos números a comparar son: ", num0, " y ", num1, "\n")
if num0 == num1:
    D1("Es igual.\n")
if num0 != num1:
    D1("Es diferente.\n")
if num0 < num1:
    D1("Es menor.\n")
if num0 > num1:
    D1("Es mayor.\n")
if num0 <= num1:
    D1("Es menor o igual.\n")
if num0 >= num1:
    D1("Es mayor o igual.\n")
D1("Fin.")

'''Algo que me dí cuenta y estoy seguro que me va a ayudar bastante, es saber que si hago una seguidilla de "if, if, if" pues, todos estos
se ejecutarán si la condición se cumple, en cambio, si es que pongo "else, else, else" pues simplemente se ejecutará UNO, si es que la 
condición especificada se cumple.''' 
