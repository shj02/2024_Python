# week12_10.py
file = "c:/abc/abc.txt"

f = None
try:
    f = open(file, "r")
except:  # 모든 Error 처리
    print(file, "이 없어요.")
finally:
    if f != None:
        f.close()

def test():
    raise NotImplementedError("구현해")

while True:
    try:
        dvd = int(input("분자:"))
        dvs = int(input("분모:"))
        result = dvd / dvs
        print(result)
        test()
    except ValueError: # 숫자가 아닌 값을 입력했을 때
        print("정수만 넣으세요.")
    except ZeroDivisionError as ze: # 0으로 나눌 때
        print(ze)   # division by zero 출력
        print("분모는 0 넣으면 안됩니다.")
    except Exception as e: # ValueError와 ZeroDivisionError 외의 에러종류를 알려줌
        print(e)
    else:
        # try구문이 정상적으로 실행되면 실행
        print("성공!")
    finally:
        print("안녕히 계세요 여러분~!")
    '''
    except Exception:   # Exception : ValueError와 ZeroDivisionError의 부모
        print("뭔가 잘못 되었네?")
    except: # 아무 오류 처리하는 except는 마지막에 넣어야 함
        print("뭔가 잘못 되었네?")
    '''

'''
try,except 넣기 전

분자:십
Traceback (most recent call last):
  File "C:/Users/PC/Desktop/week12/week12_10.py", line 3, in <module>
    dvd = int(input("분자:"))
ValueError: invalid literal for int() with base 10: '십'

분자:10
분모:0
Traceback (most recent call last):
  File "C:/Users/PC/Desktop/week12/week12_10.py", line 5, in <module>
    result = dvd / dvs
ZeroDivisionError: division by zero
'''
