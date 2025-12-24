def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def power(a,b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Modulus by zero is not allowed"
    return a % b


def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b


def calculator():
    history = []
    while True:
        print("\n====== Simple Calculator ======")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. View History")
        print("8. Clear History")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "7":
            if not history:
                print("No calculations Yet.")
            else:
                print("\n--- Calculation History ---")
                for i, item in enumerate(history, start=1):
                    print(f"{i}. {item}")
            continue

        if choice == "8":
            history.clear()
            print("History was cleared")
            continue

        if choice == "9":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4","5","6"]:
            print("Invalid choice! Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1,num2)
            record = f"{num1} + {num2} = {result}"
        elif choice == "2":
            result = subtract(num1,num2)
            record = f"{num1} - {num2} = {result}"
        elif choice == "3":
            result = multiply(num1,num2)
            record = f"{num1} * {num2} = {result}"
        elif choice == "4":
            result = divide(num1,num2)
            record = f"{num1} / {num2} = {result}"
        elif choice == "5":
            result = power(num1,num2)
            record = f"{num1} ** {num2} = {result}"
        elif choice == "6":
            result = modulus(num1,num2)
            record = f"{num1} % {num2} = {result}"
        
        if isinstance(result, str):
            print(result)
        else:
            history.append(record)
            print("Result:", result)



calculator()

