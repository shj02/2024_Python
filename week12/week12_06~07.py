# week12_06.py
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r**2)


def add(a, b):
    return a+b



# week12_07.py
import week12_06 as model
print(model.PI)

from week12_06 import PI
print(PI)

from week12_06 import PI as pi
print(pi)

print(model.add(model.PI, 4.4))

m = model.Math()
print(m.solv(2))
