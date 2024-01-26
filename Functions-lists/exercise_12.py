favorites = []

# 1. Copy your read_required_string function
# into this file.
def read_required_string(prompt):
    value = input(f"{prompt} ").strip()
    while value == "":
        print("Must provide a value")
        value = input(f"{prompt} ").strip()
    return value

# 2. Define a function that uses read_required_string
# to add a favorite (food, books, music, color, animals, whatever...)
# to the `favorites` list.
def add_favorite():
    value = read_required_string("Add your favorite book: ")
    favorites.append(value)


# 3. Define a function that prints `favorites` to the terminal.
def print_favorites():
    print(favorites)

# 4. Define a function that removes 1 to n `favorites`
# from the end of the list.
# If the argument is larger than the list length, display an error message.
# Otherwise, remove n items from the end of the list.
def remove_values():
    number = int(input("How many would you like to remove: "))
    for n in range(number):
        favorites.pop()


# 5. Define a function that displays a menu:
# ==============
# Menu
# 1. Add Favorite
# 2. Print Favorites
# 3. Remove Favorites
# 4. Exit
# Select [1-4]:
# ==============
def display_menu():
    print("="*14)
    print("1. Add Favorite")
    print("2. Print Favorites")
    print("3. Remove Favorites")
    print("4. Exit")
    print("="*14)        

# Use menu decisions to execute functions.
# Exit terminates the program.
def run_program():
    display_menu()
    value = int(input("Input a number: "))
    match value:
        case 1:
            add_favorite() 
            run_program()
        case 2: 
            print_favorites()
            run_program()
        case 3:
            remove_values()
            run_program()
        case 4: 
            return
        case _: 
            print("Please select a valid number")
            run_program()

run_program()