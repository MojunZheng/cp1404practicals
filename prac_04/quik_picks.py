import random
random_numbers = []
input_number = int(input("How many quik picks:"))
for i in range(input_number):
    for n in range(5):
        random_number = random.randint(1, 45)
        while random_number in random_numbers:
            random_number = random.randint(1, 45)
        random_numbers.append(random_number)
