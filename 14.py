# 14. Aggregation

# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.empolyee = employee

    def show_details(self):
        print(f"Department: {self.department_name}")
        self.empolyee.show()

# Independent Employee object
emp1 = Employee("Rimsha")

# Pass it to Department (aggregation)
dept1 = Department("IT", emp1)

# Use both independently
emp1.show()
dept1.show_details()
                
        