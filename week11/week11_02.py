# week11_02.py

import datetime

class Test:
    def __init__(self):
        name = ""   # 지역변수 : __init__ 종료 후 사라짐
        self.name = ""  # 멤버변수(인스턴스 변수)
        self.age = 20
        print(datetime.datetime.now()) # datetime모듈 안에 datetime클래스 안에 now()메소드가 있음
        
# 1단계 : Test() 생성자 호출
# 2단계 : __new__() 메소드 호출(인스턴스 생성), (self)쓰면 안됨
# 3단계 : __init__() 메소드 호출(인스턴스 초기화)
# 4단계 : 생성한 인스턴스 참조를 반환
t = Test()  # 인스턴스 생성
print(t.name)   # 멤버변수 출력

t2 = Test()
print(t2.name)

# t3 = t2 이게 있어도 인스턴스 개수는 2개!! 생성자를 통해서만 생성 가능

t.name = "김인하"
t2.name = "박인하"

print(t.age, t2.age)

# 메모리의 위치
print(id(t))
print(id(t2))

print(type(t) == type(t2)) # True
print(t == t2) # False 데이터(주소)가 다르기 때문
print(t.name == t2.name) # False
print(t.age == t2.age) # True 20으로 같음

# 이해용 예시
# print(type(1) == type(2))
# print(1 == 2)
