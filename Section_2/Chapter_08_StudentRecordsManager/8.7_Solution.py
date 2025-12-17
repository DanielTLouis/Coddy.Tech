student_records = dict()

def filter_top_students(threshold):
    top_students = []
    #Iterate through the student_records dictionary and find all students whose average grade is greater than the specified threshold.
    for i in student_records:
        #Use the calculate_average_grade function to get each student's average grade.
        if(calculate_average_grade(i) >= threshold):
            top_students.append(i)
    #Return a list of names of the top students.
    return top_students
    #If no students meet the criteria, return an empty list.

def list_students_by_course(course):
    #Iterate through the student_records dictionary and find all students enrolled in the specified course.
    enrolled_students = []
    for i in student_records:
        for j in student_records[i]['courses']:
            if j == course:
                enrolled_students.append(i)
    #Return a list of names of students who are enrolled in the course.
    return enrolled_students
    #If no students are enrolled in the course, return an empty list. 

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
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list
