# Create a fictional student dataset
students = [
    ["STU001", "Software Engineering", 200, 85, 78],
    ["STU002", "Computer Science", 100, 90, 82],
    ["STU003", "Cyber Security", 300, 75, 69],
    ["STU004", "Information Technology", 200, 80, 74],
    ["STU005", "Software Engineering", 100, 95, 88],
    ["STU006", "Computer Science", 300, 70, 65],
    ["STU007", "Cyber Security", 200, 88, 91],
    ["STU008", "Information Technology", 400, 92, 85],
    ["STU009", "Software Engineering", 300, 78, 72],
    ["STU010", "Computer Science", 200, 84, 80],
    ["STU011", "Cyber Security", 100, 89, 76],
    ["STU012", "Information Technology", 300, 73, 68],
    ["STU013", "Software Engineering", 400, 91, 94],
    ["STU014", "Computer Science", 100, 82, 79],
    ["STU015", "Cyber Security", 400, 86, 83],
    ["STU016", "Information Technology", 200, 77, 71],
    ["STU017", "Software Engineering", 200, 88, 86],
    ["STU018", "Computer Science", 400, 93, 90],
    ["STU019", "Cyber Security", 300, 81, 75],
    ["STU020", "Information Technology", 100, 96, 89]
]

# Define the dataset column headings
headings = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score"
]



# Display the dataset
print("FICTIONAL STUDENT DATASET")
print("-" * 90)

print(f"{'Student ID':<12} {'Department':<25} {'Level':<8} {'Attendance':<13} {'Exam Score'}")

for student in students:
    print(f"{student[0]:<12} {student[1]:<25} {student[2]:<8} {student[3]}%{'':<10} {student[4]}%")

print("-" * 90)
print("Total number of students:", len(students))
print("Dataset successfully generated")

