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

print('____Исспользование первых экземпляров____')
print()
print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()

# Задание № 4 

print('____Исспользование новых экземпляров____')
print()
print(second_reviewer)
print()
print(second_lecturer)
print()
print(second_student)
print()


def grade_student_avg(student_list, course):
    grade_stac = []
    student_grade_list = []
    for i in student_list:
        grade_stac.append(i.grades.get(course))
    for i in grade_stac:
        if type(i) is list:
            for j in i:
                student_grade_list.append(j)
    return(f'Cредняя оценка за домашние задания по всем студентам в рамках курса {course} = {sum(student_grade_list) / len(student_grade_list)}')


print(grade_student_avg([some_student, second_student], 'Python'))


def grade_lector_avg(lecturer_list, course):
    grade_stac = []
    lecturer_grade_list = []
    for i in lecturer_list:
        grade_stac.append(i.grades.get(course))
    for i in grade_stac:
        if type(i) is list:
            for j in i:
                lecturer_grade_list.append(j)
    return(f'Cредняя оценка за домашние задания по всем лекторам в рамках курса {course} = {sum(lecturer_grade_list) / len(lecturer_grade_list)}')


print(grade_lector_avg([some_lecturer, second_lecturer], 'Git'))
