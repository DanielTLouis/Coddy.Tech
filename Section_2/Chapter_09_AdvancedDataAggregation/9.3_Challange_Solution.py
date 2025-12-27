def analyze_grades(grades):
    # Write code here
    ans= dict()
    lowest_grade=100
    highest_grade=0
    student_lowest=""
    student_highest=""
    total=0
    count=0
    for i in grades:
        count+=1
        total+=grades[i]
        if(highest_grade <= grades[i]):
            highest_grade = grades[i]
            student_highest = i
        if(lowest_grade >= grades[i]):
            lowest_grade = grades[i]
            student_lowest = i
    ans["average"] = float(total) / float(count)
    ans["highest"] = highest_grade
    ans["lowest"] = lowest_grade
    ans["top_student"] = student_highest
    ans["bottom_student"] = student_lowest
    return ans

# Test the function
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)
