# Write a python program to create a function that finds a maximum of four numbers.
def find_max(num1, num2, num3, num4):
    max_num = max(num1, num2, num3, num4)
    return max_num

# Call the function with four numbers
result = find_max(10, 25, 5, 15)
print("Maximum number:", result)
