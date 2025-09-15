# Function for addition
def add(x, y):
    return x + y


# Function for subtraction
def subtract(x, y):
    return x - y


# Function for multiplication
def multiply(x, y):
    return x * y


# Function for division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


# Main calculator function
def main():
    print("Python Calculator\n")
    while True:
        print("Menu:")
        print("\t1. Addition")
        print("\t2. Subtraction")
        print("\t3. Multiplication")
        print("\t4. Division")
        print("\t5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter a valid choice (1/2/3/4/5).")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Cannot divide by zero":
                print("Error: Cannot divide by zero")
                continue
            operation = '/'

        print(f"Result: {num1} {operation} {num2} = {result}\n")


if __name__ == "__main__":
    main()
