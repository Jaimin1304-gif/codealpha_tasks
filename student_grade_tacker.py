# Student Grade Tracker Program

def input_grades():
    grades = {}
    print("\nEnter student grades for different subjects.")
    while True:
        subject = input("Enter subject name (or 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: ").strip())
            if 0 <= grade <= 100:
                grades[subject] = grade
            else:
                print("Grade should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

    return grades


def calculate_average(grades):
    if not grades:
        return 0.0
    total = sum(grades.values())
    return total / len(grades)


def display_report(grades):
    if not grades:
        print("\nNo grades entered.")
        return

    print("\nStudent Grade Report")
    print("-------------------")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

    average = calculate_average(grades)
    print(f"\nAverage Grade: {average:.2f}")

    if average >= 90:
        print("Performance: Excellent")
    elif average >= 75:
        print("Performance: Good")
    elif average >= 50:
        print("Performance: Average")
    else:
        print("Performance: Needs Improvement")


def main():
    print("\nWelcome to the Student Grade Tracker!")
    grades = input_grades()
    display_report(grades)


if __name__ == '__main__':
    main()
