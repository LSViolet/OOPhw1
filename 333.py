class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = []
        self.course = []

    def rate_lections(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached or course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

        sum = 0
        len = 0
        for key in lecturer.grades.keys():
            for val in list(lecturer.grades[key]):
                sum = sum + val
                len += 1
        lecturer.average = round(sum / len, 1)

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average} \nКурсы в процессе обучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_attached = []
        self.grades = {}
        self.average = []

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.finished_courses = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in student.grades.keys():
            for val in list(student.grades[key]):
                sum = sum + val
                len += 1
        student.average = round(sum / len, 1)

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}'


def average_comparison(lecturer, student):
    if lecturer.average > student.average:
        return 'Средняя оценка лекторов больше'
    elif student.average > lecturer.average:
        return 'Средняя оценка студентов больше'
    else:
        return 'Оценки равны'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в программирование']

best_lecturer = Lecturer('Alex', 'Polikarpov')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['GIT']
best_lecturer.courses_attached += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']
cool_reviewer.courses_attached += ['Введение в программирование']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'GIT', 1)
cool_reviewer.rate_hw(best_student, 'Введение в программирование', 1)

best_student.rate_lections(best_lecturer, 'Python', 10)
best_student.rate_lections(best_lecturer, 'GIT', 10)
best_student.rate_lections(best_lecturer, 'Введение в программирование', 1)


print(average_comparison(best_lecturer, best_student))
print(best_lecturer)
print(best_student)
print(cool_reviewer)