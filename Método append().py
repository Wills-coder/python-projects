print("Esta es una lista del abecedario: ")
lista = ["a", "b", "c", "d"]
print(lista)
while True:
    aña = input("\n¿Qué letra, número entero o flotante, o valor booleano deseas añadir a la lista?: ")
    aña = lista.append(aña)
    print(lista)