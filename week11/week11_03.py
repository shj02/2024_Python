# week11_03.py

#  필요속성이 있으면 __init__(self) 꼭 넣기!!

class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Rectangle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.width = 0.0
        self.height = 0.0

class Subject:
    def __init__(self):
        self.number = ""
        self.name = ""
        self.teacher = ""
        self.grade = 0.0

class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0

class Rectangle2:
    def __init__(self):
        self.startpoint = Point() # 위 Point 클래스를 이용해서 시작점을 구함 >> x:0 y:0
        self.width = 0.0
        self.height = 0.0

class Rectangle3:
    def __init__(self):
        self.startpoint = Point()
        self.endpoint = Point()

r2 = Rectangle2()
r3 = Rectangle3()
r2 .width = 10
r2.height = 20
print(r2.startpoint.x + r2.width)

r3.endpoint.x = 10
r3.endpoint.y = 20
print(r3.endpoint.x)
