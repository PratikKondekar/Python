students = {
    "Pratik": 85,
    "Yash": 78,
    "Sanskar": 92,
    "Vaishnavi": 88,
    "Ashwini": 74
}
student_name = input("Enter the student's name: ")
if student_name in students:
    print(f"{student_name}'s marks: {students[student_name]}")
else:
    print(f"Student not found.")
