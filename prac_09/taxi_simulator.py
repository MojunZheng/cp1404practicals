from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>>"
def main():
    """Main function controlling the taxi simulation process"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = get_valid_taxi_choice(taxis, taxi_choice)
        elif choice == "d":
            trip_cost = drive_taxi(current_taxi)
            total_bill += trip_cost
        else:
            print("Invalid choice")
        print(f"Bill to date: ${total_bill:.2f}")
        choice = input(MENU).lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)
