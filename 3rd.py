class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_history(self):
        if not self.history:
            print("No operations performed yet.")
        else:
            print("\n--- Operation History ---")
            for item in self.history:
                print(item)


def main():
    calc = Calculator()

    while True:
        print("\nCalculator Menu")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", calc.add(a, b))
            elif choice == "2":
                print("Result:", calc.subtract(a, b))
            elif choice == "3":
                print("Result:", calc.multiply(a, b))
            elif choice == "4":
                print("Result:", calc.divide(a, b))

        elif choice == "5":
            calc.show_history()

        elif choice == "6":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
