class GradeBook:
    """ЗАДАЧА: Найти имя студента с самым высоким средним баллом"""
    def __init__(self): self.students = {} # {"Ivan": [5, 4], "Oleg": [3]}
    def get_best_student(self):
        best_student = None
        highest = 0
        for name, grades in self.students.items():
            sred = sum(grades) / len(grades)
            if sred > highest:
                highest = sred
                best_student = name
        return best_student