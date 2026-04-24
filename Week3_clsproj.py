students = {
	"Alice": [95, 87, 92],
	"Bob": [78, 82, 85],
	"Todd": [84, 85, 92],
	"Kyle": [96, 98, 99],
	"Remy": [65, 68, 71],
	"Sharon": [89, 75, 77]}

def get_average(grades_list):
    return sum(grades_list) / len(grades_list) if grades_list else 0

def get_highest(grades_list):
    return max(grades_list) if grades_list else None

def get_lowest(grades_list):
    return min(grades_list) if grades_list else None

def add_student(name, grade):
    if name in students:
        return False
    students[name] = [grade]
    return True

def add_grade(name, grade):
    if name not in students:
        return False
    students[name].append(grade)
    return True

def get_class_average(students_dict):
    averages = [get_average(grades) for grades in students_dict.values() if grades]
    return sum(averages) / len(averages) if averages else 0

def display_report(students_dict):
    print("\nSTUDENT GRADE REPORT")
    print("-" * 40)
    for name, grades in students_dict.items():
        avg = get_average(grades)
        hi = get_highest(grades)
        lo = get_lowest(grades)
        print(f"{name:<12} Grades: {str(grades):<20} Avg: {avg:>6.2f}  High: {hi:>3}  Low: {lo:>3}")
    print("-" * 40)
    print(f"Class Average: {get_class_average(students_dict):.2f}")

def main():
    while True:
        print("\n  Class Grades Menu  ")
        print("=" * 40)
        print(" (A)dd student     ")
        print(" (G)rade a student ")
        print(" (S)hows stats     ")
        print(" (E)xit            ")
        print("=" * 40)

        choice = input("Choose an option: ").strip().upper()

        if choice == "A":
            name = input("Student name: ").strip()
            try:
                grade = float(input("Initial grade: ").strip())
            except ValueError:
                print("Invalid grade.")
                continue

            if add_student(name, grade):
                print(f"Added {name}.")
            else:
                print("Student already exists.")

        elif choice == "G":
            name = input("Student name: ").strip()
            try:
                grade = float(input("New grade: ").strip())
            except ValueError:
                print("Invalid grade.")
                continue
            if add_grade(name, grade):
                print(f"Added grade for {name}.")
            else:
                print("Student not found.")

        elif choice == "S":
            display_report(students)

        elif choice == "E":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()