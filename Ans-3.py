# Write a python program to create a function which expects an unknown number of arguments.
def print_arguments(*args):
    for arg in args:
        print("Argument:", arg)

# Call the function with different number of arguments
print_arguments("Hello", "World")
print_arguments(1, 2, 3, 4, 5)
print_arguments(True, "Python", 3.14)
