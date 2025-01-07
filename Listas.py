while True:

    name = input("Name: ").capitalize()
    age = input("Age: ")
    height = input("Height: ")
    studentornot = input("Are you a student? (Y/N): ").lower()


    if studentornot == "y":
        studentornot = True
    elif studentornot == "n":
        studentornot = False
    else:   
        print("Not a valid option.")
        studentornot = "?"

    data = [name, age, height, studentornot]

    print(data)

    another = input("Do you want to continue with another list? (Y/N): ").lower()
    if another == "y":
        another = True
    elif another == "n":
        another = False
        print("ok, bye then, see u next time. ;)")
        break
    else:
        print("not an option, we will continue the list btw.")
