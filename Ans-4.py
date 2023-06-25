# Write a python program to create a function which expects kwargs arguments.
def print_arguments(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Call the function with different keyword arguments
print_arguments(name="John", age=30)
print_arguments(city="New York", country="USA", population=8537673)
print_arguments(language="Python", version=3.9, framework="Django")
