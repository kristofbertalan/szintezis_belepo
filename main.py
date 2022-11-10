from ExamPlace import ExamPlace
from Examiner import Examiner
from Manager import Manager

examplace = ExamPlace()
man = Manager("John", 21, 0)
emp = Examiner("Dave", 10, 0)
examplace.hire_employee(emp, man)
print(examplace.listofEmployees)