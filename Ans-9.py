# Write a python program to create a function to check whether a number falls in a given range.
def check_range(number, lower, upper):
    if number >= lower and number <= upper:
        return True
    else:
        return False

# Example usage
num = 25
lower_limit = 10
upper_limit = 50

if check_range(num, lower_limit, upper_limit):
    print(f"The number {num} falls within the range of {lower_limit} and {upper_limit}.")
else:
    print(f"The number {num} does not fall within the range of {lower_limit} and {upper_limit}.")
