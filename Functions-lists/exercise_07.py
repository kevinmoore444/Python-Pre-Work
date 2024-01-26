values = [34, 47, 84, 19, 54, 19, 89, 68, 0, 93, 87, 44, 97, 79]
# 1. Create a new list named `evens`.
evens = []
# 2. Loop over the `values` list. If the value is even,
for value in values:
    if value%2 == 0:
        evens.append(value)

# add it to the `evens` list.
# 3. Print `evens`.
print(evens)
# Expected output:
# [34, 84, 54, 68, 0, 44]
