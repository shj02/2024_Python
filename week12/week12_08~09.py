# week12_08.py
def add(a, b):
    return a+b

if __name__ == "__main__":
    print(add(1,2))
# else: print(__name__)



# week12_09.py
import week12_08 as m
print(m.add(10,20))
