
history = []


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def show_history():
    print("\n===== CALCULATION HISTORY =====")

    if len(history) == 0:
        print("No calculations yet.")
    else:
        for item in history:
            print(item)


def calculator():
    print("================================")
    print("       PYTHON CALCULATOR")
    print("================================")

    while True:
        print("\nChoose an option:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. View History")
        print("6. Clear History")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "7":
            print("Thank you for using Python Calculator!")
            break

        if choice == "5":
            show_history()
            continue

        if choice == "6":
            history.clear()
            print("History cleared!")
            continue

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice! Select 1 to 7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"

        else:
            result = divide(num1, num2)
            symbol = "/"

            if result is None:
                print("Error! Cannot divide by zero.")
                continue

        print("Result:", result)

        calculation = f"{num1:g} {symbol} {num2:g} = {result:g}"
        history.append(calculation)


if __name__ == "__main__":
    calculator()
