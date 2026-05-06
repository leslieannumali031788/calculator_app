from rich.console import Console
console = Console()

class Calculator:
    def add(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number

class OtherOperations(Calculator):
    def multiply(self, first_number, second_number):
        return first_number * second_number

    def divide(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError
        return first_number / second_number

def get_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")

def main():

    calculator = OtherOperations()

    while True:

        print("\n===== Calculator =====")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")

        choice = input("\nEnter your choice: ")

        first_number = get_input("\nEnter first number: ")
        second_number = get_input("\nEnter second number: ")

        try:
            if choice == "1":
                result = calculator.add(first_number, second_number)

            elif choice == "2":
                result = calculator.subtract(first_number, second_number)

            elif choice == "3":
                result = calculator.multiply(first_number, second_number)

            elif choice == "4":
                result = calculator.divide(first_number, second_number)

            else:
                print("Please enter a valid choice.")
                continue

            print("The result is: ", result)

        except ZeroDivisionError:
            print("You can't divide by zero. Please try again.")

        again = input("\nDo you want to try again? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using calculator. See you next time!")
            break

if __name__ == "__main__":
    main()
