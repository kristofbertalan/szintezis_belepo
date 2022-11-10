import unittest
from ExamPlace import ExamPlace
from Examiner import Examiner
from Manager import Manager
from Car import Car
from Person import Person
from Exam import Exam
from datetime import date

class testExamPlace(unittest.TestCase):
    def test_hire_employee(self):
        examplace = ExamPlace()
        man = Manager("John", 21, 0)
        emp = Examiner("Dave", 10, 0)
        examplace.hire_employee(emp, man)
        self.assertIn(emp, examplace.listofEmployees)

    def test_fire_employee(self):
        examplace = ExamPlace()
        man = Manager("John", 21, 0)
        emp = Examiner("Dave", 10, 0)
        examplace.hire_employee(emp, man)
        examplace.fire_employee(emp)
        self.assertNotIn(emp, examplace.listofEmployees)

    def test_approve_exam(self):
        pers = Person("Bela", 1234)
        car = Car("BMW", "G12", pers)
        emp = Examiner("Dave", 10, 0)
        examplace = ExamPlace()
        result = examplace.approveExam(car, emp)
        ex = Exam(date.today().strftime("%d/%m/%Y"), "successful", car, emp)
        self.assertEqual(result, ex)

    def test_fail_exam(self):
        pers = Person("Bela", 1234)
        car = Car("BMW", "G12", pers)
        emp = Examiner("Dave", 10, 0)
        examplace = ExamPlace()
        result = examplace.failExam(car, emp)
        ex = Exam(date.today().strftime("%d/%m/%Y"), "failed", car, emp)
        self.assertEqual(result, ex)



