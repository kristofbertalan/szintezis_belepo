class Employee:

    def __init__(self, name, emp_code, hired_by):
        self.name = name
        self.emp_code = emp_code
        self.hired_by = hired_by

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_emp_code(self):
        return self.emp_code

    def set_emp_code(self, emp_code):
        self.emp_code = emp_code

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.emp_code == other.get_emp_code()
        return False
