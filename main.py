class Student:
    """
    Class to represent the student.
    ...
    Attributes
    --------
    name : str
        person's name
    surname : str
        person's surname
    gender : str
        sex of a person
    finished_courses : list
        list of completed courses
    courses_in_progress : list
        courses in progress
    grades : dict
        Dictionary with grades for homework.
        keys - are course titles, values - are grade lists
    Methods
    ------
    rate_hw(self, lecturer, course, grade):
        Adds the lecturer's grade to the list of his grades for a specific course.
    average():
        Calculates the average student grade for all courses
    """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Задание № 2.
    def rate_hw(self, lecturer, course, grade):
        """
        Students give grades to lecturers. The assigned grade is added to the lecturer's list of grades for the course.
        The lecturer must belong to the class of lecturers, be assigned to the course for which the student is enrolled.
        :param lecturer: lecturer class instance
        :param course: name of the training course
        :param grade: grade for a lecture
        :return: If the conditions are not met, it returns "Error", otherwise it adds a grade for the course to the lecturer.
        """
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание № 3.1
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.average()}'
                f'\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {",".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average() < other.average()

    def average(self):
        """
        Calculates the average student grade for all courses.
        :return: the student's average grade in all courses.
        """
        sum_hw = 0
        count = 0
        for grade in self.grades.values():
            sum_hw += sum(grade) / len(grade)
            count += 1
        return round(sum_hw / count, 2)


class Mentor:
    """
    A class representing a mentor.
    ...
    Attributes
    --------
    name : str
        person's name
    surname : str
        person's surname
    courses_attached : list
        List of assigned courses
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Задание № 1. (лекторы)
class Lecturer(Mentor):
    """
    The class representing the lecturer. It is a child of the Mentor class.
    ...
    Attributes
    --------
    grades : dict
        Dictionary with grades for lectures.
        keys - course names, values - grade lists
    Methods
    ------
    average():
        Calculates the lecturer's average grade for lectures
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Задание № 3.1
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.average()}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average() < other.average()

    def average(self):
        """
        Calculates the lecturer's average grade for lectures.
        :return: the lecturer's average grade for lectures.
        """
        sum_hw = 0
        count = 0
        for grade in self.grades.values():
            sum_hw += sum(grade) / len(grade)
            count += 1
        return round(sum_hw / count, 2)


# Задание № 1. (эксперты, проверяющие домашние задания)
class Reviewer(Mentor):
    """
    The class representing the lecturer. It is a child of the Mentor class.
    ...
    Methods
    ------
    rate_hw(self, student, course, grade):
        Adds a student's homework grade to his list of grades for a specific course.
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Задание № 2. Выставлять студентам оценки за домашние задания
    def rate_hw(self, student, course, grade):
        """
        Reviewers give grades to students. The assigned grade is added to the student's grade list for the course.
        The student must belong to the class of students, enrolled in the course and the course is incomplete.
        :param student: student class instance
        :param course: name of the training course
        :param grade: homework grade
        :return: If the conditions are not met, it returns "Error", otherwise it adds a grade for homework to the student.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание № 3.1
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


# Создаем по 2 экземпляра каждого класса
best_student = Student('Ivan', 'Ivanov', 'male')
best_student.courses_in_progress += ['Python']
good_student = Student('Anna', 'Petrova', 'female')
good_student.courses_in_progress += ['Git']

class_lecturer = Lecturer('Kirill', 'Korshunov')
class_lecturer.courses_attached += ['Python']
kind_lecturer = Lecturer('Aleksandr', 'Sidorov')
kind_lecturer.courses_attached += ['Git']

cool_reviewer = Reviewer('Stepan', 'Penkin')
cool_reviewer.courses_attached += ['Python']
strict_reviewer = Reviewer('Vladimir', 'Bondarev')
strict_reviewer.courses_attached += ['Git']

# Закрепляем курсы
best_student.finished_courses = ['Введение в программирование']
best_student.courses_in_progress = ['Python', 'Git']
good_student.finished_courses = ['Введение в программирование']
good_student.courses_in_progress = ['Python', 'Git']

class_lecturer.courses_attached = ['Введение в программирование', 'Python', 'Git']
kind_lecturer.courses_attached = ['Введение в программирование', 'Python', 'Git']
cool_reviewer.courses_attached = ['Введение в программирование', 'Python', 'Git']
strict_reviewer.courses_attached = ['Введение в программирование', 'Python', 'Git']

# Задание № 2. Студенты ставят оценки лекторам
best_student.rate_hw(class_lecturer, 'Python', 8)
best_student.rate_hw(class_lecturer, 'Python', 9)
best_student.rate_hw(class_lecturer, 'Python', 7)
best_student.rate_hw(class_lecturer, 'Git', 9)
best_student.rate_hw(class_lecturer, 'Git', 9)
best_student.rate_hw(class_lecturer, 'Git', 10)

best_student.rate_hw(kind_lecturer, 'Python', 9)
best_student.rate_hw(kind_lecturer, 'Python', 9)
best_student.rate_hw(kind_lecturer, 'Python', 10)
best_student.rate_hw(kind_lecturer, 'Git', 10)
best_student.rate_hw(kind_lecturer, 'Git', 4)
best_student.rate_hw(kind_lecturer, 'Git', 10)

good_student.rate_hw(class_lecturer, 'Python', 5)
good_student.rate_hw(class_lecturer, 'Python', 10)
good_student.rate_hw(class_lecturer, 'Python', 9)
good_student.rate_hw(class_lecturer, 'Git', 8)
good_student.rate_hw(class_lecturer, 'Git', 8)
good_student.rate_hw(class_lecturer, 'Git', 9)

good_student.rate_hw(kind_lecturer, 'Python', 7)
good_student.rate_hw(kind_lecturer, 'Python', 9)
good_student.rate_hw(kind_lecturer, 'Python', 8)
good_student.rate_hw(kind_lecturer, 'Git', 9)
good_student.rate_hw(kind_lecturer, 'Git', 9)
good_student.rate_hw(kind_lecturer, 'Git', 10)

# Ревьюверы ставят оценки студентам
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(good_student, 'Python', 7)
cool_reviewer.rate_hw(good_student, 'Python', 8)
cool_reviewer.rate_hw(good_student, 'Python', 5)
cool_reviewer.rate_hw(good_student, 'Git', 7)
cool_reviewer.rate_hw(good_student, 'Git', 6)
cool_reviewer.rate_hw(good_student, 'Git', 10)

strict_reviewer.rate_hw(best_student, 'Python', 10)
strict_reviewer.rate_hw(best_student, 'Python', 9)
strict_reviewer.rate_hw(best_student, 'Python', 7)
strict_reviewer.rate_hw(best_student, 'Git', 6)
strict_reviewer.rate_hw(best_student, 'Git', 9)
strict_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(good_student, 'Python', 9)
cool_reviewer.rate_hw(good_student, 'Python', 9)
cool_reviewer.rate_hw(good_student, 'Python', 10)
cool_reviewer.rate_hw(good_student, 'Git', 10)
cool_reviewer.rate_hw(good_student, 'Git', 9)
cool_reviewer.rate_hw(good_student, 'Git', 10)

print('\nПечатаем оценки студентов по курсам')
print(f'{best_student.surname} {best_student.name}: {best_student.grades}')
print(f'{good_student.surname} {good_student.name}: {good_student.grades}')

print('\nПечатаем оценки лекторов по курсам')
print(f'{class_lecturer.surname} {class_lecturer.name}: {class_lecturer.grades}')
print(f'{kind_lecturer.surname} {kind_lecturer.name}: {kind_lecturer.grades}')

print('\nСравниваем лекторов по средней оценке')
msg = (f'Средняя оценка лектора {class_lecturer.surname} {class_lecturer.name}: '
       f'{class_lecturer.average()} < '
       f'Средняя оценка лектора {kind_lecturer.surname} {kind_lecturer.name}: '
       f'{kind_lecturer.average()} = {class_lecturer.average() < kind_lecturer.average()}')
print(msg)

msg = (f'Средняя оценка лектора {class_lecturer.surname} {class_lecturer.name}: '
       f'{class_lecturer.average()} > '
       f'Средняя оценка лектора {kind_lecturer.surname} {kind_lecturer.name}: '
       f'{kind_lecturer.average()} = {class_lecturer.average() > kind_lecturer.average()}')
print(msg)

print('\nСравниваем студентов по средней оценке')
msg = (f'Средняя оценка студента {best_student.surname} {best_student.name}: '
       f'{best_student.average()} < '
       f'Средняя оценка студента {good_student.surname} {good_student.name}: '
       f'{good_student.average()} = {best_student.average() < good_student.average()}')
print(msg)

msg = (f'Средняя оценка студента {best_student.surname} {best_student.name}: '
       f'{best_student.average()} > '
       f'Средняя оценка студента {good_student.surname} {good_student.name}: '
       f'{good_student.average()} = {best_student.average() > good_student.average()}')
print(msg)

# Задание № 3.1
print('\nПечатаем информацию согласно Задания №3.1 - студенты')
print(best_student)
print('-')
print(good_student)
print('\nПечатаем информацию согласно Задания №3.1 - лекторы')
print(class_lecturer)
print('-')
print(kind_lecturer)
print('\nПечатаем информацию согласно Задания №3.1 - ревьюверы')
print(cool_reviewer)
print('-')
print(strict_reviewer)

students_list = [best_student, good_student]
lecturer_list = [class_lecturer, kind_lecturer]
reviewer_list = [cool_reviewer, strict_reviewer]

print('\nСписок студентов')
for student in students_list:
    print(student.name, student.surname, student.gender, student.finished_courses, student.courses_in_progress, student.grades)

print('\nСписок лекторов')
for lecturer in lecturer_list:
    print(lecturer.name, lecturer.surname, lecturer.courses_attached, lecturer.grades)

print('\nСписок ревьюверов')
for reviewer in reviewer_list:
    print(reviewer.name, reviewer.surname, reviewer.courses_attached)


def avg_hw_students_in_course(students, course):
    """
    Calculates a student's average grade for homework assignments across all courses
    :param students: student class instance
    :param course: name of the training course
    :return: Returns the student's average grade for homework assignments across all courses
    """
    sum_hw = 0
    count = 0
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                sum_hw += sum(value) / len(value)
                count += 1
    return round(sum_hw / count, 2)


def avg_hw_lecturer_in_course(lecturers, course):
    """
    Calculates the lecturer's average grade for all lectures.
    :param lecturers: экземпляр класса лектор
    :param course: name of the training course
    :return: Returns the lecturer's average grade for lectures across all courses
    """
    sum_hw = 0
    count = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                sum_hw += sum(value) / len(value)
                count += 1
    return round(sum_hw / count, 2)


print('\nСредние оценки по курсам')
print('Средняя оценка студентов по курсу Python: ', avg_hw_students_in_course(students_list, 'Python'))
print('Средняя оценка студентов по курсу Git: ', avg_hw_students_in_course(students_list, 'Git'))
print('Средняя оценка лекторов по курсу Python: ', avg_hw_lecturer_in_course(lecturer_list, 'Python'))
print('Средняя оценка лекторов по курсу Git: ', avg_hw_lecturer_in_course(lecturer_list, 'Git'))
