plates = []

def read_required_int(prompt):
    try:
        value = input(prompt).strip()
        return int(value)
    except:
        print("Error: Please input a valid number")


def run():
    option = ""
    while option != 0:
        print("")
        print("MENU")
        print("="*12)
        print("0. [Exit]")
        print("1. Add a plate")
        print("2. Print plates")
        print("3. Remove plates")
        option = read_required_int("Select [0-3]: ")
        match option:
            case 0:
                print("Goodbye")
            case 1:
                add_a_plate()
            case 2:
                print_plates()
            case 3: 
                remove_plates()
            case _:
                print("Please select a valid number")


def add_a_plate():
    print("")
    print("Add a Plate")
    print("=" *12)
    new_plate = read_required_int("Enter a Plate Size: ")
    try:
        if new_plate<0:
            print("Plate size must be a positive integer")
        elif len(plates) == 0 and isinstance(new_plate, int) or plates[-1] >= new_plate:
            plates.append(new_plate)
        else: 
            print(f"Error. Cannot place a plate of size {new_plate} on top of another plate of size {plates[-1]}")
    except:
        print("")

    
def print_plates():
    print("")
    print("Print Plates")
    print("="*12)
    if len(plates) == 0:
        print("There are no stacked plates")
    else:
        for plate in reversed(plates):
            print(("#"*plate).center(10))

def remove_plates():
    print("")
    print("Remove Plates")
    print("="*12)
    plates_to_remove = read_required_int("How many plates do you want to remove?: ")
    try:
        if len(plates) < plates_to_remove:
            print(f"Error: Cannot remove more than {len(plates)} plates. You chose {plates_to_remove}")
        else:
            for n in range(plates_to_remove):
                plates.pop()
            print("")
            print("Success!")
    except:
        print("")


run()

