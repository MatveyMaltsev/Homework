def top(input_data):
    parts = input_data.split("student_")[1:]
    results = {}
    for part in parts:
        student_num = int(part) // 100
        grade = int(part) % 100
        results[student_num] = grade
    highest_grade = max(results.values())
    return [student for student, grade in results.items() if grade == highest_grade]

s = input()
top_students = top(s)

for student in top_students:
    print(student)
