# week09_01.py

data1 = [1,2,3,4]

summary  = sum(data1)
maximum = max(data1)
minimum = min(data1)
average = summary/len(data1)

print(summary)
print(maximum)
print(minimum)
print(average)

print("-" * 30)

for d in data1:
    print(d)

print("-" * 30)

for i in range(0, 4):
    print(i)

print("-" * 30)

for d in range(len(data1)):
    print(d)

print("-" * 30)

for d in range(len(data1)):
    print(f"data1[{d}]:{data1[d]}")

print("-" * 30)

for d in enumerate(data1):      # d의 타입 : tuple
    print(f"data1[{d[0]}]:{d[1]}")

for i, d in enumerate(data1):   # 변수 2개
    print(f"data1{[i]}:{d}")

data2 = [[1,2,3,4], [10,20,30,40], [11,12,13,14]]

print("-" * 30)

for d1 in data2:
    print(d1)

print("-" * 30)

for d1 in data2:
    print("sum", sum(d1))       # !!!
    print("max", max(d1))
    print("min", min(d1))
    print("avg", summary/len(d1))
    print("-")

for i1, d1 in enumerate(data2):   # 변수 2개
    print(f"{i1+1}번째 : {d1}")
    print("sum", sum(d1))       
    print("max", max(d1))
    print("min", min(d1))
    print("avg", summary/len(d1))
    print("-")

for i1, d1 in enumerate(data2):     # !!!
    print(f"{i1+1}번째 : ", end="")
    for i2, d2 in enumerate(d1):
        print(f"[{i2+1}]{d2} ", end="")
    print()
    print("sum", sum(d1))       
    print("max", max(d1))
    print("min", min(d1))
    print("avg", summary/len(d1))
    print("-")

data3 = {   "김인하" : [1,2]
            ,   "이인하" : [10,20,30,40,50,60,70]
            ,   "송인하" : [11,12,13,14]
            }

print("-" * 30)

for d1 in data3:    # key / .key()
    print(d1)

print("-" * 30)

for d1 in data3:    # !!!
    print(data3[d1])

print("-" * 30)

for d1 in data3:    # !!!
    print(f"{d1}:{data3[d1]}")

for i1, d1 in enumerate(data3):     # !!!
    print(f"{d1} : ", end="")
    for i2, d3 in enumerate(data3[d1]):
        print(f"[{i2+1}]{d3} ", end="")
    print()
    print("sum", sum(data3[d1]))       
    print("max", max(data3[d1]))
    print("min", min(data3[d1]))
    print("avg", summary/len(data3[d1]))
    print("-")
