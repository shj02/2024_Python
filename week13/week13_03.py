# week13_03
# id : 202444040
# name : son hyeji

# file -> text file
# datetime -> str -> 저장
# 읽기 -> str -> datetime
from datetime import datetime as dt

# %Y : 연도 / %m : 월 / %d : 일
# %H : 시간 / %M : 분 / %S : 초 / %f : 마이크로세컨드

dtformat = "%Y-%m-%d %H:%M:%S.%f"

d = dt.now() # type(d) -> datetime.datetime
d1 = dt.strftime(d, dtformat) # f : format / datetime -> str
d2 = dt.strptime(d1, dtformat) # p : parse / str(d1) -> datetime(d2)

print(type(d), d) # type : datetime
print(type(d1), d1) # type : str
print(type(d2), d2) # type : datetime.datetime
