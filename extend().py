inv = ["Juan","Gerardo","Luciana"]
frd = ["Luis","Ana"]
print(f"Lista invitados: {inv} \nLista de amigos: {frd}")
inv.extend(frd)
print(f"Lista invitados: {inv}")

numeros = [10,20]
print(f"\nLista números: {numeros}")
numeros.extend(range(30,100,10))
print(f"Lista números: {numeros}")