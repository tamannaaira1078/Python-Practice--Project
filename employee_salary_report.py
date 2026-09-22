from collections import namedtuple
from functools import wraps

Employee = namedtuple("Employee", ["name", "role", "salary"])


employees = [
    Employee("Aira", "Junior Developer", 90000),
    Employee("Fera", "Backend Developer", 80000),
    Employee("Riza", "Graphic Designer", 50000)
]


def high_earners(employees, minimum_salary):
    for emp in employees:
        if emp.salary>=minimum_salary:
            yield emp
           


def announce(original_function):
    @wraps(original_function)
    
    def wrapper(*args, **kwargs):
        print("Generating salary report...")
        result=original_function(*args, **kwargs)
        return result
    return wrapper


@announce
def show_report(employees, minimum_salary):
    earners_generator = high_earners(employees, minimum_salary) 
    for emp in earners_generator:
        print(f"{emp.name} - {emp.role} - {emp.salary}") 


while True:
    try:
        user_input = int(input("Enter minimum salary: "))  
        break
    except ValueError:
        print("Please Enter a valid input") 
          
show_report(employees, user_input)          