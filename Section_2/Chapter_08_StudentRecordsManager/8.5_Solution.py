student_records = dict()

def calculate_average_grade(name):
    #Check if the student name exists in the student_records dictionary.
    if name not in student_records:
        #If it does not exist, print "Student '<name>' not found." and return None.
        print(f"Student '{name}' not found.")
    #If the name exists, calculate the average of the grades in the student's grades set.
    else:
        #If the grades set is empty, return 0.
        if(not student_records[name]['grades']):
            return 0
        #Otherwise, calculate and return the average grade as a float.
        else: 
            total = 0
            count = 0
            for i in student_records[name]['grades']:
                total += i
                count += 1
            return float(float(total)/float(count))

def is_enrolled(name, course):
    if name in student_records:
        if course in student_records[name]['courses']:
            #student is enrolled 
            return True
        else:
            #student not in course
            return False
    else:
        print(f"Student '{name}' not found.")
        return False

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
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again
