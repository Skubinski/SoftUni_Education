# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    return principal * rate * time

# Function to calculate Compound Interest
def calculate_compound_interest(principal, annual_rate, compounds_per_year, time):
    monthly_rate = annual_rate / (12 * 100)
    return principal * (1 + monthly_rate / compounds_per_year) ** (compounds_per_year * time) - principal

# Function to calculate Loan Payment (EMI)
def calculate_loan_payment(principal, annual_rate, loan_tenure_years):
    monthly_rate = annual_rate / (12 * 100)
    loan_tenure_months = loan_tenure_years * 12
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -loan_tenure_months)

# Function to calculate Future Value of Savings with regular contributions
def calculate_future_value_of_savings(principal, annual_rate, contributions_per_year, time, contributions):
    monthly_rate = annual_rate / (12 * 100)
    total_months = time * 12
    future_value = 0

    for month in range(total_months):
        future_value += contributions
        future_value *= (1 + monthly_rate / contributions_per_year)

    return future_value

# Main menu function
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Calculate Simple Interest")
        print("2. Calculate Compound Interest")
        print("3. Calculate Loan Payment")
        print("4. Calculate Future Value of Savings")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            print("\nCalculate Simple Interest")
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter interest rate (as a decimal): "))
            time = float(input("Enter time (in years): "))
            simple_interest = calculate_simple_interest(principal, rate, time)
            print(f"Simple Interest: ${simple_interest:.2f}")

        elif choice == '2':
            print("\nCalculate Compound Interest")
            principal = float(input("Enter principal amount: "))
            annual_rate = float(input("Enter annual interest rate (as a decimal): "))
            compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))
            time = float(input("Enter time (in years): "))
            compound_interest = calculate_compound_interest(principal, annual_rate, compounds_per_year, time)
            print(f"Compound Interest: ${compound_interest:.2f}")

        elif choice == '3':
            print("\nCalculate Loan Payment")
            principal = float(input("Enter principal amount: "))
            annual_rate = float(input("Enter annual interest rate (as a percentage): "))
            loan_tenure_years = float(input("Enter the loan tenure in years: "))
            loan_payment = calculate_loan_payment(principal, annual_rate, loan_tenure_years)
            print(f"Monthly Loan Payment (EMI): ${loan_payment:.2f}")

        elif choice == '4':
            print("\nCalculate Future Value of Savings")
            principal = float(input("Enter principal amount: "))
            annual_rate = float(input("Enter annual interest rate (as a percentage): "))
            contributions_per_year = int(input("Enter the number of contributions per year: "))
            time = float(input("Enter time (in years): "))
            contributions = float(input("Enter monthly contributions: "))
            future_value = calculate_future_value_of_savings(principal, annual_rate, contributions_per_year, time, contributions)
            print(f"Future Value of Savings: ${future_value:.2f}")

        elif choice == '5':
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a valid option (1/2/3/4/5).")

        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main_menu()
