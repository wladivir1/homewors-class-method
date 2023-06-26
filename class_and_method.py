class Student:
    """ Student class: adds a list of completed courses, grades lecturers """
    
    def __init__(self, name, surname):
        self.name = name                # имя
        self.surname = surname          # фамилия
        self.finished_courses = []      # список оконченных курсов
        self.courses_in_progress = []   # спиок курсов 
        self.grades = {}                # оценка
    
    def add_courses(self, course_name):
        """ adds completed courses to the list """
        self.finished_courses.append(course_name)    
        
    def rate_lecturer(self, lecture, course, grade):
        """ Gives grades to lecturers """
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached \
                and course in self.courses_in_progress \
                and 0 < grade < 10:
            if course in lecture.grades_lecture:
                lecture.grades_lecture[course] += [grade]
            else:
                lecture.grades_lecture[course] = [grade]           
        else:
            return 'Ошибка'
        
    def __str__(self):
        """ Overrides values """
        some_student = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за задание: {average_grade(self.grades)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return some_student
    
    def __lt__(self, other_student):
        """ Produces a greater than, less than comparison """
        if isinstance(other_student, Lecturer):
            return average_grade(self.grades) < average_grade(other_student.grades_lecture)    
 
    
class Mentor:
    """ Parent class Mentors: contains only attributes """
    def __init__(self, name, surname):
        self.name = name             # имя
        self.surname = surname       # фамилия
        self.courses_attached = []   # список курсов       


class Lecturer(Mentor):
    """ Lecturer class: inherits the Mentor class, receives grades from students """
    def __init__(self, name, surname):
        super().__init__(name, surname)    
        self.grades_lecture = {}
        
    def __str__(self):
        """ Overrides values """
        some_lecturer = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades_lecture)}"
        return some_lecturer    
    
    def __lt__(self, other_lecturer):
        """ Produces a greater than, less than comparison """
        if isinstance(other_lecturer, Lecturer):
            return average_grade(self.grades_lecture) < average_grade(other_lecturer.grades_lecture)    
 
       
class Reviewer(Mentor):
    """ Expert class: grades students """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    
    def rate_hw(self, student, course, grade):
        """ Gives grades to students """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]              
        else:
            return 'Ошибка' 
    
    def __str__(self):
        """ Overrides values """
        some_reviewer = f"Имя: {self.name}\nФамилия: {self.surname}"
        return some_reviewer    
        

def average_grade(all_grades):
    """ The function of calculating the average value of grades """
    if type(all_grades) is dict:
        amout_grades = []
        for grades in all_grades.values():
            for grade in grades:
                amout_grades.append(grade)
        return average_grade(amout_grades)
    elif type(all_grades) is list and all_grades[0] != None:
        average = round(sum(all_grades) / len(all_grades), 2)
        return average         
    else:
        return 'Ошибка'


def average_course_grade(all_students, current_course):
    """ The function of calculating the average value of grades """
    all_course_grades = []
    for current_student in all_students:
        if current_course in current_student.grades.keys():
            for every_grade in current_student.grades.get(current_course):
                all_course_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у студента: {current_student.name} {current_student.surname}')
    return average_grade(all_course_grades)        

def average_lecturers_grade(all_lecturers, current_course):
    """ Data collection function to calculate the average value of lecturers' grades """
    all_lecturers_grades = []
    for current_lecturers in all_lecturers:
        if current_course in current_lecturers.grades_lecture.keys():
            for every_grade in current_lecturers.grades_lecture.get(current_course):
                all_lecturers_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у лектора: {current_lecturers.name} {current_lecturers.surname}')
    return average_grade(all_lecturers_grades)

        
# Создание экземпляра класса студент1:
student_no_1 = Student('Roy', 'Eman')
student_no_1.courses_in_progress += ['Python']
student_no_1.courses_in_progress += ['English for IT']
student_no_1.finished_courses += ['Git']
student_no_1.add_courses('Math')
student_no_1.grades['Git'] = [7, 2, 6]
student_no_1.grades['Python'] = [10, 10, 8, 10, 10, 10]
student_no_1.grades['English for IT'] = [10, 10]

# Создание экземпляра класса студент2:
student_no_2 = Student('Mike', 'Red')
student_no_2.courses_in_progress += ['Python']
student_no_2.finished_courses += ['Git']
student_no_2.grades['Git'] = [9, 5, 2]
student_no_2.grades['Python'] = [8, 10]

# Допустим мы их храним в списке (для функции average_course_grade):
student_list = [student_no_1, student_no_2]

# Создание экземпляра класса лектор1:
lecturer_1 = Lecturer('Bill', 'Boops')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['English for IT']
lecturer_1.courses_attached += ['Git']
lecturer_1.grades_lecture['Git'] = [2, 6, 9, 10, 10]
lecturer_1.grades_lecture['Python'] = [10, 6, 8, 10, 10]
lecturer_1.grades_lecture['English for IT'] = [5, 6, 2, 10, 10]

# Создание экземпляра класса лектор2:
lecturer_2 = Lecturer('Ray', 'Bitts')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['English for IT']
lecturer_2.courses_attached += ['Git']
lecturer_2.grades_lecture['Git'] = [5, 6, 8, 10, 10]
lecturer_2.grades_lecture['Python'] = [4, 7, 8, 9, 10]
lecturer_2.grades_lecture['English for IT'] = [5, 6, 8, 10, 1]

# Допустим мы их храним в списке (для функции average_lecturers_grade):
lecturer_list = [lecturer_1, lecturer_2]

# Создание экземпляра класса Эксперт:
cool_reviewer = Reviewer('Anton', 'Green')
cool_reviewer.courses_attached += ['Python']

# Создание экземпляра класса Эксперт2:
cool_reviewer_2 = Reviewer('Eddy', 'Grey')
cool_reviewer_2.courses_attached += ['Git']

# Проверяем
print('----Вывод результатов----')
print(lecturer_2)
print()
print(cool_reviewer)
print()
print(student_no_1)
print()
print(student_no_2)
print()

print('----Рассчет среднего балла студентов по определенному курсу----')
print(average_course_grade(student_list, 'Git'))
print()

print('----Рассчет среднего балла лекторов----')
print(average_lecturers_grade(lecturer_list, 'Git'))
print()



       