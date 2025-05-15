# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee():

    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp1 = Employee("Rimsha", 75000, "123-45-6789")  

# Public variable access
print("Name:", emp1.name)

# Private variable access
print("Salary:", emp1._salary)

try:
    print("SSN:", emp1.__ssn)
except AttributeError:
    print("SSN: Cannot access __ssn directly (it's private)")  

# Trick to access private (not recommended)
print("SSN (accessed via name mangling):", emp1._Employee__ssn)              