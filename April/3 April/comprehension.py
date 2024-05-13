# values = [1,2,3,4]

# new_values = []

# for value in values:
#     new_values.append(value**2)

# print(new_values)

# Comprehension

# values = [1,2,3,4]

# new_values = [value**2 for value in values]
# print(new_values)

values = [1,2,3,4]

# new_values = []

# for value in values:
#     if value % 2 == 0:
#         new_values.append(value**2)

# print(new_values)

# new_values = [value**2 for value in values if value % 2 == 0]

# print(new_values)


new_values = []

for value in values:
    if value % 2 == 0:
        new_values.append(value**2)
    else:
        new_values.append(value)

print(new_values)

new_values = [value**2 if value % 2 == 0 else value for value in values]

print(new_values)