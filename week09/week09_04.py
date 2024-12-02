# week09_04.py

s1 = set("abbbbc")
print(s1)

s2 = set([1,2,2,2,3,3,3,4,-1, 'a'])
print(s2)

# set -> 중복 X, 순서 X

s3 = s1 & s2    # 교집합
print(s3)

s4 = s1 | s2    # 합집합
print(s4)

s5 = s1 - s2    # 차집합
print(s5)

s5.add('q')    # 단일 요소 추가
print(s5)

# s6 = s5.add('q') -> None : set의 add 메소드는 집합에 요소를 추가한 후 None을 반환함 -> s5에는 'q'가 추가되지만 s6에는 None이 저장됨

s5.update(['b', 10])  # 여러 요소 추가
print(s5)

s5.remove('b')
print(s5)
