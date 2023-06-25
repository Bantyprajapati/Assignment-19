# Write a python program to create a function to check whether a given number is even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 25

result = check_even_odd(num)
print(f"The number {num} is {result}.")
