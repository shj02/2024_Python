# week12_01.py

class Subject:  # Subject() --> __new__() --> __init()__
    def __init__(self, number, name, teacher=None, grade=None): # grade=-1도 가능
        self.number = number
        self.name = name
        self.teacher = teacher
        self.setGrade(grade)

    def __str__(self):
        return f"[{self.number}] {self.name}"

    def setGrade(self, grade):
        if grade != None:
            if grade < 0:
                grade = 0.0
            elif grade > 4.5:
                grade = 4.5
        self.grade = grade

sub1 = Subject("0001", "컴퓨터공학분석", grade=1000.9)
print(sub1.grade)

sub1.grade = 1000.9
print(sub1.grade)    # 1000.9가 나옴

sub1.setGrade(1000.9)
print(sub1.grade)    # 4.5가 나옴

print("***")

class Student:
    def __init__(self, number, name, dept, birthyear, *subjects): # *가변매개변수(튜플)
        self.number = number
        self.name = name
        self.dept = dept
        self.birthyear = birthyear
        if subjects:
            self.subjects = list(subjects)    # subjects를 리스트로 변환하고 저장
        else:
            self.subjects = list()            # 빈 리스트 저장
    def __str__(self):
        return f"[{self.number}] {self.name}"

    def total_grade(self):
        if self.subjects:
            grades = [subject.grade for subject in self.subjects if subject.grade != None]
                        # list comprehension
            if grades:
                return sum(grades) / len(grades)
        else:
            # print("수강과목이 없음")
            return None

sub1 = Student("1", "손혜지", "컴정", 2005)
print(sub1)
print(sub1.total_grade())

sub2 = Student("2", "박혜지", "컴정", 2005,
                Subject("1", "파이썬", "장은미"),
                Subject("2", "자바스크립트", "전혜경")
                )
print(sub2)
print(sub2.total_grade())

sub3 = Student("3", "혜지", "컴정", 2005,
                Subject("1", "파이썬", "장은미", 4.5),
                Subject("2", "자바스크립트", "전혜경", 2.0),
                Subject("3", "오픈소스", "김태간")
                )
print(sub3)
print(sub3.total_grade())
