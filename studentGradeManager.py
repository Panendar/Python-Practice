students = {
    "Alice": {"math": 85, "science": 92, "english": 88},
    "Bob": {"math": 78, "science": 81, "english": 75},
    "Charlie": {"math": 90, "science": 95, "english":92},
    "David": {"math": 70, "science": 68, "english": 72},
    "Eve": {"math": 88, "science": 84, "english": 90}
}
def student_average(name):
    if name in students:
        grades =students[name].values()
        average =sum(grades)/len(grades)
        return average
    else:
        print("Student not recorded.")

student_name = input("Enter the student's name to calculate average grade: ").capitalize()
print(f"Student's name {student_name}: \n{students[student_name]} recorded.")
print(f"The average grade of {student_name} is: {student_average(student_name):.2f}")
print("========================================")
def top_performer():
    top = max(student_average("Alice"), student_average("Bob"), student_average("Charlie"), student_average("David"), student_average("Eve"))
    for name in students:
        if student_average(name) == top:
            print(f"The Top scorer is: {name} {top:.2f}")
            return name

top_scorer = input("Do you want to see the top scorer? (Yes/No): ").capitalize()
if top_scorer == "Yes":
    top_performer()
    print("========================================")
else:
    print("HAVE A GOOD DAY! THANK YOU! ========================")

def class_average():
    sum = 0
    for student_name in students:
        sum = sum + student_average(student_name)
        avg = sum /len(students)
    print(f"The class average is: {avg:.2f}")

class_avg = input("DO you want to see the class average? (Yes/No):").capitalize()
if class_avg == "Yes":
    class_average()
    print("========================================")
else:
    print("HAVE A GOOD DAY! THANK YOU! ========================")

def students_above_80():
    print("Students with average grade above 80:")
    for student_name in students:
        if student_average(student_name) > 80:
            print(f"{student_name} - Average Grade: {student_average(student_name):.2f}")

above_80 = input("Do you want to see students with average grade above 80? (Yes/No): ").capitalize()
if above_80 == "Yes":
    students_above_80()
    print("========================================")
else:
    print("HAVE A GOOD DAY! THANK YOU! ========================")