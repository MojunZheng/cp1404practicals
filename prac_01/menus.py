def display_menu():
    print("H, Print Hello")
    print("G, print Goodbye")
    print("Q, Exit")

name= input ("name")

choice = ''
while choice != 'Q':
    display_menu()
    choice = input("Make the choice: ").upper()

    if choice == 'H':
        print("Hello,", name)
    elif choice == 'G':
        print("Goodbye,", name)
    elif choice == 'Q':
        print("exit")
    else:
        print("Try again")

print("End")