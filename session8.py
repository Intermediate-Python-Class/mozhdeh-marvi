# You are a teacher at a high school, and you have recently conducted an exam for a class of students. 
# Each student's exam grade is represented by a tuple (student_name, score),
# where student_name is a string representing the student's name,
# and score is an integer representing the exam score (out of 100). 
# Your task is to sort the students' exam grades based on their scores in ascending order. 
# If two or more students have the same score, they should be sorted alphabetically by their names.
# Write a Python function to solve this problem.



def sort_students(students):
    sorted_stds = sorted(students, key=lambda  student: (student[1] , student[0]))         
    return sorted_stds


students = [
    ('Mzhd' , 100),
    ('sahar' , 98),
    ('Khalid' , 99),
    ('Hasib' , 99),
    ('Fatimah' , 76),
    ('Hasti' , 85),
    ('Amin' , 94),
]

sorted_stds = sort_students(students)
for student in sorted_stds:
    print(student)