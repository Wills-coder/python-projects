print("center:")
string = "MENÚ"
print(string.center(20))

print("ljust:")
print(string.ljust(20))

print("rjust:")
print(string.rjust(20))

print("\nMétodos con caracteres:")
print("center:")
string = "MENÚ"
print(string.center(20, "="))

print("ljust:")
print(string.ljust(20, "="))

print("rjust:")
print(string.rjust(20, "="))

print("Variable modificada:")
string = string.center(10, "=")
print(string)
