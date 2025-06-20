"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

first_initials = [name[0] for name in names]
print(first_initials)

full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

a_names = [name for name in names if name.startswith('A')]
print(a_names)

print(" ".join(sorted(names)))

lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

numbers = [int(number) for number in almost_numbers]
print(numbers)

greater_numbers = [number_greater for number_greater in numbers if number_greater > 9]
print(greater_numbers)

last_names = []
long_names = [l_name for l_name in full_names if len(l_name) > 11]
for full_name in long_names:
    name_parts = full_name.split()
    last_name = name_parts[-1]
    last_names.append(last_name)
print(" ".join(last_names))
