def average(numbers):
    total = 0
    for i in numbers:
        total += i
    return round(total / len(numbers),2)
def transform_dataset(data):
    # Your solution here
    
    # Step 1: Calculate average grade for each student and filter qualified students
    # (students with all grades above 70)
    averages = dict()
    for i in data:
        if all( x > 70 for x in i["grades"]):
            avg = average(list(i["grades"]))
            averages[i["student_id"]] = avg
    # Step 2: Create a summary of subjects taken by qualified students
    bucket = dict()
    for i in data:
        if all( x > 70 for x in i["grades"]):
            for j in i["subjects"]:
                if j in bucket:
                    bucket[j] += 1
                else:
                    bucket[j] = 1
    summary = dict()
    summary["qualified_students"] = averages
    summary["subject_summary"] = bucket
    # Step 3: Return the final dictionary with qualified_students and subject_summary
    return summary 
    
    pass
