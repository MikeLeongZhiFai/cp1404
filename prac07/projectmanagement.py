import datetime

from prac_07.project import Project

MENU = "- (L)oad Projects\n- (S)ave Projects\n- (D)isplay Projects\n- (F)ilter by Date\n- (A)dd new Project\n- (U)pdate Project\n- (Q)uit"

def main():
    print(MENU)
    menu_choice = input(">>> ").title()
    while menu_choice != "Q":
        if menu_choice == "L":
            projects_list = load_file()
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "S":
            save_file(projects_list)
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "D":
            display_projects(projects_list)
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "F":
            date_filtering(projects_list)
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "A":
            add_project(projects_list)
            print(MENU)
            menu_choice = input(">>> ").title()
        elif menu_choice == "U":
            update_project(projects_list)
            print(MENU)
            menu_choice = input(">>> ").title()
        else:
            print("Invalid Input")
            print(MENU)
            menu_choice = input(">>> ").title()
    print("Thank you for using custom-built project management software.")


def load_file():
    projects_file = input("Project file: ")
    try:
        with open(projects_file, "r") as file:
            project_list = []
            file.readline()
            for current_line in file:
                parts = current_line.strip().split(' ')
                current_project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                project_list.append(current_project)
        return project_list
    except FileNotFoundError:
        project_list = []
        return project_list


def save_file(projects_list):
    projects_file = input("Project file: ")
    with open(projects_file, "w") as file:
        file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
        for current_line in projects_list:
            writing_line = " ".join(current_line)
            file.write(writing_line)


def display_projects(projects_list):
    # Sort the projects by completion status
    incomplete_projects = []
    completed_projects = []
    for project in projects_list:
        if not project.is_complete():
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)

    # Print the incomplete projects
    print("Incomplete Projects:")
    if incomplete_projects:
        for project in incomplete_projects:
            print(project)
    else:
        print("No incomplete projects.")

    # Print the completed projects
    print("\nCompleted Projects:")
    if completed_projects:
        for project in completed_projects:
            print(project)
    else:
        print("No completed projects.")


def date_filtering(projects_list):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        date_filter = datetime.datetime.strptime(date_string, "%d/%m/%Y")
        filtered_list = [project for project in projects_list if
                         datetime.datetime.strptime(project.start_date, "%d/%m/%Y") > date_filter]
        print("Filtered Projects:")
        if filtered_list:
            for project in filtered_list:
                print(project)
        else:
            print("No projects found.")
    except ValueError:
        print("Invalid date format.")


def add_project(projects_list):
    name = input("Enter project name: ")
    start_date_string = input("Enter project start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").strftime("%d/%m/%Y")
        priority = int(input("Enter project priority (1-5): "))
        cost_estimation = float(input("Enter project cost estimation: "))
        completion_percentage = float(input("Enter project completion percentage: "))
        new_project = Project(name, start_date, priority, cost_estimation, completion_percentage)
        projects_list.append(new_project)
        print("New project added.")
    except ValueError:
        print("Invalid input.")


def update_project(projects_list):
    print("Select a project to update:")
    for i, project in enumerate(projects_list):
        print(f"{i + 1}: {project}")
    try:
        selection = int(input("Enter project number: "))
        if 1 <= selection <= len(projects_list):
            project = projects_list[selection - 1]
            print(f"Updating project: {project}")
            new_completion_percentage = float(input("Enter new completion percentage: "))
            new_priority = int(input("Enter new priority: "))
            project.completion_percentage = new_completion_percentage
            project.priority = new_priority
            print("Project updated.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")


main()