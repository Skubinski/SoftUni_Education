def create_loading_bar(number):
    if number < 0 or number > 100 or number % 10 != 0:
        return "Invalid input"

    progress = number // 10
    loading_bar = f"{number}% [{'%' * progress}{'.' * (10 - progress)}]"

    if number == 100:
        return f"100% Complete! \n[%%%%%%%%%%]"
    else:
        return loading_bar + "\nStill loading..."

# Example usage:
input_number = int(input())
result = create_loading_bar(input_number)
print(result)
