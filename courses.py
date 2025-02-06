class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lesson(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress and grade in grade_list:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}   

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)   
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade in grade_list:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

grade_list = list(range(1,11))

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_rev = Reviewer('Some', 'Buddy')
cool_rev.courses_attached += ['Python']

best_lector = Lector('Ivan', 'Andreev')

cool_rev.rate_hw(best_student, 'Python', 8)
cool_rev.rate_hw(best_student, 'Python', 9)
cool_rev.rate_hw(best_student, 'Python', 10)

best_student.rate_lesson(best_lector, 'Python', 8)

print(best_student.name, best_student.grades)
print(best_lector.name, best_lector.grades)