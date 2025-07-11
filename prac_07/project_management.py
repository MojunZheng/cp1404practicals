from project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit\n>>>")
FILE_NAME = "projects.txt"
LOAD = "l"
SAVE = "s"
DISPLAY = "d"
FILTER = "f"
ADD = "a"
UPDATE = "u"
QUIT = "q"
MAXIMUM_PERCENTAGE = 100
MINIMUM_PERCENTAGE = 0


def main():
    """Call and pass data to the functions below"""
    projects = read_file(FILE_NAME)
    choice = input(MENU).lower()
    while choice != QUIT:
        if choice == LOAD:
            load_file("What file do you want to load?")
        elif choice == SAVE:
            get_file_name(projects)
        elif choice == DISPLAY:
            display_projects(projects)
        elif choice == FILTER:
            filter_projects(projects)
        elif choice == ADD:
            add_project(projects)
        elif choice == UPDATE:
            update_project(projects)
        else:
            print("Invalid input")
        choice = input(MENU).lower()
    save_option = input("Do you want to save your file?(Y/N)").lower()
    if save_option == "y":
        save_projects(projects, FILE_NAME)
    print("Thank you for using custom-built project management software.")
