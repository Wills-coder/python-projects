
#Sum() sirve para sumar números dentro de una lista.


num = [1,2,3]
print(num)
print(sum(num))

num = [1,2,3]
print(f"Con valor inicial: 10 \n{num}")
print(sum(num,10))

num = [1,2,3]
print(f"Con valor inicial: -2 \n{num}")
print(sum(num,-2))

num = [1,2.5,True]
print(f"\n{num}")
print(sum(num))

num = [1,2.5,"a"]
print(f"\n{num}") #Error de intentar combinar un string.
print(sum(num))