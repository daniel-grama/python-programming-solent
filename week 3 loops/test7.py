while True:
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Total:", result)

    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Total:", result)

    elif choice == 3:
        print("Exit")
        break

    else:
        print("Try correct number")
