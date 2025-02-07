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
    
    def avg(self): # Подсчет среднего значения всех оценок
        self.gradeStatistic = []
        for val in self.grades.values():
            [self.gradeStatistic.append(i) for i in val]      
        self.average = sum(self.gradeStatistic) / len(self.gradeStatistic)
        return self.average
        
    def __str__(self): # Добавлен магический метод __str__ (задание 3)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avg()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg(self): # Подсчет среднего значения всех оценок
        self.gradeStatistic = []
        for val in self.grades.values():
            [self.gradeStatistic.append(i) for i in val]      
        self.average = sum(self.gradeStatistic) / len(self.gradeStatistic)
        return self.average

    def __str__(self): # Добавлен магический метод __str__ (задание 3)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avg()}\n')

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
    
    def __str__(self): # Добавлен магический метод __str__ (задание 3)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

grade_list = list(range(1,11))

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_lecturer = Lector('Some', 'Buddy')

some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)


some_student.rate_lesson(some_lecturer, 'Python', 8)

# print(some_student.name, some_student.grades)
# print(some_lecturer.name, some_lecturer.grades)

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)