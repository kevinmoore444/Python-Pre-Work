# Read Required String
# ====================

# 1. Define a function that reads a value from a user
# and issues a warning if the value is blank (whitespace) or empty.
# Re-prompt the user.
# If the value is not blank or empty, return it.
# (Hint: use a loop.)
# 
# Name: read_required_string
# Inputs: str (prompt to the user)
# Output: str (a non-blank, non-empty string)

def read_required_string(prompt, error):
    value = input(f"{prompt} ").strip()
    while value == "":
        print(error)
        value = input(f"{prompt} ").strip()
    return value
# Example
# value = read_required_string("Favorite food?: ")
#
# Favorite food?:
# Value is required.
# Favorite food?:
# Value is required.
# Favorite food?:
# Value is required.
# Favorite food?: spaghetti

favorite_food = read_required_string("Favorite Food", "A Food is Required")
print(f"Your favorite food is {favorite_food}")
favorite_book = read_required_string("Favorite Book", "A Book is Required")
print(f"Your favorite book is {favorite_book}")