all_student = {}
between_10_and_0 = {}
between_17_and_20 = {}


def search_student(student):
    if student in all_student:
        print(f"{student}'s grede: {all_student[student]}")
    else:
        print(f"Student {student} not found")


with open("grade_students.csv") as f:
    for line in f:
        student_name, grade = line.strip().split(",")
        grade = int(grade)
        all_student[student_name] = grade
        if 17 <= grade <= 20:
            between_17_and_20[student_name] = grade
        elif 0 <= grade <= 10:
            between_10_and_0[student_name] = grade

print(f"all_student: {all_student}")
print(f"between_17_and_20: {between_17_and_20}")
print(f"between_10_and_0: {between_10_and_0}")
student = input("Enter student name:")
search_student(student)

