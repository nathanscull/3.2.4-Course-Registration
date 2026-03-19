done = False

def assignment1():
    print("Assignment 1 Completed")

def assignment2():
    print("Assignment 2 Completed")

while not done:
    assignment_number = input("1, 2 or quit? ")

    if assignment_number == "1":
        assignment1()
    elif assignment_number == "2":
        assignment2()
    elif assignment_number == "quit":
        done = True
    else:
        print("Invalid input. Please enter 1, 2 or quit.")
