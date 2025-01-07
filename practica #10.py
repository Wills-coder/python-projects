#Práctica diez:

num = []
long = int(input("¿Cuántos números enteros contendrá la lista?: "))
for _ in range(long): 
    num.append(int(input("Introduce un número entero: ")))

print(f"\nLista; {num} \nLa suma total es: {sum(num)}")