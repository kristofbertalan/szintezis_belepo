class Exam:

    def __init__(self, date, result, car, examiner):
        self.date = date
        self.result = result
        self.car = car
        self.examiner = examiner

    def __str__(self):
        return f"Exam(date={self.date}, result={self.result}, car={self.car}, examiner={self.examiner})"

    def __repr__(self):
        return f"Exam(date={self.date}, result={self.result}, car={self.car}, examiner={self.examiner})"

    def __eq__(self, other):
        if isinstance(other, Exam):
            return self.date == other.date and self.result == other.result \
                   and self.car == other.car \
                   and self.examiner == other.examiner
        return False
