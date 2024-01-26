# Mad Libs
# https://en.wikipedia.org/wiki/Mad_Libs

# 1. Copy your read_required_string function
# definition into this file.

def read_required_string(prompt):
    value = input(f"{prompt} ").strip()
    while value == "":
        print("Must provide a value")
        value = input(f"{prompt} ").strip()
    return value

# 2. Define a mad_lib function.
# Collect three required strings from the user:
# `adjective`, `verb`, and `noun`.
# Use them to print this message.
# f"The {adjective} squirrel {verb} away with the {noun}."
# (You can certainly get more creative with your Mad Libs.)
def mad_lib():
    noun = read_required_string("State a noun")
    verb = read_required_string("State a verb")
    adjective = read_required_string("State an adjective")
    print(f"The {adjective} squirrel {verb} away with the {noun}. ")

mad_lib()


# 3. Call the mad_lib function at least three times.
