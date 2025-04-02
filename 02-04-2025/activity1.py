def calculator():
    while True:
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Floor Division (//)")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")
        
        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {num1 ** num2}")
            elif choice == '6':
                if num2 != 0:
                    print(f"Result: {num1} // {num2} = {num1 // num2}")
                else:
                    print("Error: Floor division by zero is not allowed.")
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

calculator()

