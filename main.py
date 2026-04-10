done = False
def assignment1():
    print("Assignment 1 Completed")
def assignment2():
    return("Assignment 2 Completed")
def execute_assignment(assignment_number):
    global done
    if assignment_number == "1":
        assignment1()
    elif assignment_number == "2":
        print(assignment2())
    elif assignment_number == "quit":
        done = True
    else:
        print("Invalid input. Please enter 1, 2, or quit.")
while not done:
    assignment_number = input("Enter 1 or 2 or quit: ")

    execute_assignment(assignment_number)