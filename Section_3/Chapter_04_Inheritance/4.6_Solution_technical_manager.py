from manager import Manager
from engineer import Engineer
from person import Person 

class TechnicalManager(Manager, Engineer):
    class_name = "Technical Manager"
    def __init__(self, name, age, employee_id, salary, department, programming_language):
        # Initialize Person directly
        Person.__init__(self, name, age)
        
        # Set remaining attributes
        self.employee_id = employee_id
        self.salary = salary 
        self.department = department
        self.programming_language = programming_language
    
