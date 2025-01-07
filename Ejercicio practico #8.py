#Tabla de multiplicar:

import time
def dinput(text, delay=0.04):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay) 
    return input()

while True:

    num = int(input("¿Qué tabla de multiplicar deseas ver?: "))

    print(f"La tabla del {num} es:")


    for mult in range(1,11):
        print(f"{num} x {mult} = {num*mult}")

