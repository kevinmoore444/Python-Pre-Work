numbers = []

# 1. Define a function that accepts an integer argument.
# If the `numbers` list is empty, add the argument to the list.
# If the last element in the `numbers` list is greater than the integer
# argument, don't append it.
# If the last element is less than or equal to the
# integer argument, append it to the list.
#
# There are two options:
# 1. Use the `numbers` list in file scope.
# This would require only one parameter - the value.
# 2. Pass the `number` list as an argument.
# This would require two parameters - the integer list and the value.
#
# Option #1
# Name: add_valid_int
# Inputs: int (value to add)
# Output: None
# numbers = []
def add_valid_int(value):
    if not numbers or value < numbers[-1]:
        numbers.append(value)
    


#
# Option #2
# Name: add_valid_int
# Inputs: list[int] (the `number` list), int (value to add)
# Output: None
        
def add_valid_int(list, value):
    if not list or value < list[-1]:
        list.append(value)


# Option #1
add_valid_int(4)
print(numbers)  # [4]
add_valid_int(3)
print(numbers)  # [4, 3]
add_valid_int(14)
print(numbers)  # [4, 3]
#
# Option #2
add_valid_int(numbers, 4)
print(numbers)  # [4]
add_valid_int(numbers, 3)
print(numbers)  # [4, 3]
add_valid_int(numbers, 14)
print(numbers)  # [4, 3]
