student_records = dict()

def add_student(name, age, course):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name]= {'age':age, 'grades':set(), 'courses':course}
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name in student_records:
        student_records[name]['grades'].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    else:
        print(f"Student '{name}' not found.") 

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(student_records)
