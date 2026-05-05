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

    print("\n===== Calculator =====")