from Employee import Employee

class Manager(Employee):

    def __init__(self, name, emp_code, hired_by):
        super().__init__(name, emp_code, hired_by)
