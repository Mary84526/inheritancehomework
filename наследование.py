class Student:


def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

    def lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.grades_lecturers:
                lecturer.grades_lecturers[course] += [grade]
            else:
                lecturer.grades_lecturers[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturers = {}
        def avarage_grade(self):
            all_grades = []
            for grades in self.grades_lecturers.values():
                all_grades += grades
                avarage_grade = sum(all_grades) / len(all_grades)
                return avarage_grade

    def __str__(self):
        some_lecturer = f'Имя:{self.name} \n Фамилтя:{self.surname} \n Средняя оценка за лекции:'
        some_lecturer = f'{self.avarage_grade}'
        return some_lecturer

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = {}
    def rate_hm(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def __str__(self):
    some_reviewer = f'Имя:{self.name} \n Фамилтя:{self.surname}'
    return some_reviewer
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


