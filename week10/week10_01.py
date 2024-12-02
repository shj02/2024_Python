# week10_01.py

mydir = "c:\\202444040\\sonhyeji.txt"   # txt 파일 생성

# 자원 접근 (열기)
# f = open(mydir, 'w')      w : 쓰기모드(무조건 새로)
f = open(mydir, 'a')        # 추가모드

# 작업
f.write("손혜지\n")

# 자원 해제 (닫기)
f.close()


f1 = open(mydir, 'r')   # 읽기모드
print(f1.read())    # 작업(메모장 내용 print)
f1.close()      # 닫기
