from Employee import Employee

class Examiner(Employee):

    def __init__(self, name, emp_code, hired_by):
        super().__init__(name, emp_code, hired_by)

    def __str__(self):
        return f"Examiner(name={self.name}, emp_code={self.emp_code}, hired_by={self.hired_by}"

    def __repr__(self):
        return f"Examiner(name={self.name}, emp_code={self.emp_code}, hired_by={self.hired_by}"
