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


def read_file(file_name):
    """Reads project data from projects CSV file"""
    projects = []
    with open(file_name, "r") as projects_information:
        projects_information.readline()
        for line in projects_information:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))  # use Project class to install project data to the list
            projects.append(project)
        print(f"Loaded {len(projects)} projects from {file_name}")
    return projects


def load_file(input_name):
    """Load specified file or default file"""
    file_name = input(input_name)
    try:
        read_file(file_name)
    except FileNotFoundError:
        print(f"File not found, open default file--{FILE_NAME}")
        read_file(FILE_NAME)


def get_file_name(projects):
    """Get specified file name"""
    user_input_name = input("Input name:")
    if not user_input_name.endswith(".txt"):
        user_input_name += ".txt"
    save_projects(projects, user_input_name)


def save_projects(projects, file_name):
    """Save projects to specified file"""
    with open(file_name, 'w') as new_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=new_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.percentage}", file = new_file)
    print(f"{len(projects)} projects saved to {file_name}")
