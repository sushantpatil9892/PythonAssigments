students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 90
}

name = input("Enter the student's name: ")
marks = students.get(name)

if marks is not None:
    print(f"{name}'s marks: {marks}")
else:
    print("Student not found.")