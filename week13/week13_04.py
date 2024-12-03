# week13_04
# id : 202444040
# name : son hyeji

import datetime as dt

d1 = dt.datetime(2030, 10, 2, 18, 0, 2, 200)
d2 = dt.datetime(2031, 10, 3, 17, 3, 3, 202)

t = d2 - d1
print(type(t)) # datetime.timedelta
print(t)
print(t.days)
# 시랑 분은 없음
# print(t.hours)
# print(t.minutes)
print(t.seconds) # days를 빼고 남은 시간들만!
print(t.microseconds)

print(t.total_seconds()) # 전체 시간들을 초단위로!

d3 = d1 + dt.timedelta(days=29)
d4 = d1 + dt.timedelta(days=-29)
print(d3)
print(d4)
