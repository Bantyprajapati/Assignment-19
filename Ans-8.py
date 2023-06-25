# Write a python program to multiply all the numbers in a list.
def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
my_list = [1, 2, 3, 4, 5]
result = multiply_numbers(my_list)
print("Product of numbers:", result)
