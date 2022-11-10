from datetime import date
from Exam import Exam


class ExamPlace:

    listofEmployees = []
    listofManagers = []


    def hire_employee(self, employee, manager):
        employee.hired_by = manager.get_emp_code()
        self.listofEmployees.append(employee)

    def fire_employee(self, emp):
        for employee in self.listofEmployees:
            if employee == emp:
                self.listofEmployees.remove(employee)

    def approveExam(self, car, examiner):
        return Exam(date.today().strftime("%d/%m/%Y"), "successful", car, examiner)

    def failExam(self, car, examiner):
        return Exam(date.today().strftime("%d/%m/%Y"), "failed", car, examiner)




