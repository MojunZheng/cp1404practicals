name = input("Enter your name：")
with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    name = file.read()
    print(f"Hi {name}!")

with open("numbers.txt", "r") as file:
    number_1 = int(file.readline())
    number_2 = int(file.readline())
    print(number_1 + number_2)

