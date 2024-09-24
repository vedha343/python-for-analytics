# Student Grade Management System

# Function to calculate grade based on the total score
def calculate_grade(total_score):
    if total_score >= 90:
        return 'A'
    elif total_score >= 80:
        return 'B'
    elif total_score >= 70:
        return 'C'
    elif total_score >= 60:
        return 'D'
    else:
        return 'F'

# Function to display all student details
def display_students(student_list):
    print("\nStudent Information:")
    print("---------------------------------------------------")
    print("Name\t\tID\t\tTotal Score\tGrade")
    print("---------------------------------------------------")
    for student in student_list:
        print(f"{student['name']}\t\t{student['id']}\t\t{student['total_score']}\t\t{student['grade']}")
    print("---------------------------------------------------\n")

# Function to add student details to the list
def add_student(student_list):
    name = input("Enter student's name: ")
    student_id = input("Enter student's ID: ")

    scores = []
    for i in range(3):  # Assuming 3 subjects
        score = int(input(f"Enter score for subject {i+1}: "))
        scores.append(score)

    total_score = sum(scores)
    grade = calculate_grade(total_score)

    student = {
        'name': name,
        'id': student_id,
        'total_score': total_score,
        'grade': grade
    }

    student_list.append(student)
    print(f"Student {name} added successfully!\n")

# Main function
def main():
    student_list = []

    while True:
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_student(student_list)
        elif choice == '2':
            display_students(student_list)
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
