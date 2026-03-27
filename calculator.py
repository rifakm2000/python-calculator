n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
while True:
    print("\n1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Modulo")
    print("5-Exponentiation")
    print("6-Floor Division")
    print("7-Division")
    print("8-Exit")

    choice = int(input("Select your choice (1-8): "))

    if choice == 1:
        print("Addition:", n1 + n2)

    elif choice == 2:
        print("Subtraction:", n1 - n2)

    elif choice == 3:
        print("Multiplication:", n1 * n2)

    elif choice == 4:
        print("Modulo:", n1 % n2)

    elif choice == 5:
        print("Exponentiation:", n1 ** n2)

    elif choice == 6:
        if n2 != 0:
            print("Floor Division:", n1 // n2)
        else:
            print("Cannot divide by zero")

    elif choice == 7:
        if n2 != 0:
            print("Division:", n1 / n2)
        else:
            print("Cannot divide by zero")

    elif choice == 8:
        print("Exit")
        break

    else:
        print("Invalid choice")
