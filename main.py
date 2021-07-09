class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, grade, course):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in list(lecturer.grades.keys()):
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = list()
                lecturer.grades[course].append(grade)
        else:
            print('ошибка')

    def __str__(self):
        sums = 0
        counter = 0
        course_in_progress_str = str()
        finished_course_str = str()
        for course in self.courses_in_progress:
            course_in_progress_str = f'{course_in_progress_str} {course},'
        for course in self.finished_courses:
            finished_course_str = f'{finished_course_str} {course},'
        for grade in self.grades.values():
            for grades in grade:
                sums += grades
                counter += 1
        if counter == 0:
            return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {0}
Курс в процессе изучения: {course_in_progress_str[:-1]}
Завершенные курсы: {finished_course_str[:-1]}'''
        else:
            return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {round(sums/counter, 1)}
Курс в процессе изучения: {course_in_progress_str[:-1]}
Завершенные курсы: {finished_course_str[:-1]}'''

    def __lt__(self, other):
        if isinstance(other, Student):
            sums = 0
            summs = 0
            counter = 0
            counter1 = 0
            for grade in self.grades.values():
                for grades in grade:
                    sums += grades
                    counter += 1
            for grade in other.grades.values():
                for grades in grade:
                    summs += grades
                    counter1 += 1
            return sums/counter < summs/counter1
        else:
            print('ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        sums = 0
        counter = 0
        for grade in self.grades.values():
            for grades in grade:
                sums += grades
                counter += 1
        if counter == 0:
            return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {0}'''
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {round(sums/counter, 1)}'''


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''

def average_grade_students(students, course):
    avg_grade = 0
    counter = 0
    for student in students:
        avg_grade += sum(student.grades[course])
        counter += len(student.grades[course])
    return round(avg_grade/counter, 1)

def average_grade_lecturers(lecturers, course):
    avg_grade = 0
    counter = 0
    for lecturer in lecturers:
        avg_grade += sum(lecturer.grades[course])
        counter += len(lecturer.grades[course])
    return round(avg_grade/counter, 1)


reviewer1 = Reviewer('vasia', 'pupkin')
reviewer2 = Reviewer('vasia', 'pupkin')
student1 = Student('vasia', 'pupkin', 'man')
student2 = Student('vasia', 'pupkin', 'man')
lecturer1 = Lecturer('vasia', 'pupkin')
lecturer2 = Lecturer('vasia', 'pupkin')
student1.courses_in_progress.append('python')
student2.courses_in_progress.append('python')
lecturer1.courses_attached.append('python')
lecturer2.courses_attached.append('python')
reviewer1.courses_attached.append('python')
reviewer2.courses_attached.append('python')
student1.rate(lecturer1, 10, 'python')
student1.rate(lecturer2, 10, 'python')
reviewer1.rate_hw(student1, 'python', 9)
reviewer1.rate_hw(student2, 'python', 10)
if student1 > student2:
    print('у первого ученика оценки выше')
else:
    print('у второго ученика оценки выше')
print(student1)
print(lecturer1)
print(reviewer1)
print(average_grade_students([student1, student2], 'python'))
print(average_grade_lecturers([lecturer1, lecturer2], 'python'))

