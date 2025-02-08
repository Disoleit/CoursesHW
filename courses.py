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
                f'Средняя оценка за лекции: {self.avg()}\n')

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
    
class Statistic:
    def __init__(self, person, course):
        self.personList = person
        self.course = course
        self.courseGradeList = []

    def lecturerStat(self):
        for person in self.personList:
            if person.grades().key() == self.course:
                # добавить значения по ключу в courseGradeList
                # посчитать avg по формуле
                # return lecturer_avg_grade

        pass

    def studentStat(self):
        # student_avg_grade = {}
        # return student_avg_grade
        pass

    # функция на вход принимаем список студентов и название курса def([some_student, second_student] Git)

    # функция на вход принимаем список лекторов и название курса def([some_lecturer, second_lecturer] Git)

grade_list = list(range(1,11))

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

second_student = Student('Kate', 'Eman', 'your_gender')
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в программирование']
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

second_reviewer = Reviewer('Petr', 'Petrov')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

some_lecturer = Lector('Some', 'Buddy')

second_lecturer = Lector('Ivan', 'Ivanov')

some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)

second_reviewer.rate_hw(second_student, 'Git', 10)

some_student.rate_lesson(some_lecturer, 'Python', 8)

second_student.rate_lesson(second_lecturer, 'Git', 8)

# print(some_student.name, some_student.grades)
# print(some_lecturer.name, some_lecturer.grades)

# print('____Исспользование первых экземпляров____')
# print()
# print(some_reviewer)
# print()
# print(some_lecturer)
# print()
# print(some_student)
# print()
# print('____Исспользование новых экземпляров____')
# print()
# print(second_reviewer)
# print()
# print(second_lecturer)
# print()
# print(second_student)
# print()
# print('____6754____')
# print(Student.__name__)