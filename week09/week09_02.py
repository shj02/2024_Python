# week09_02.py

data2 = [[1,2,3,4], [10,20,30,40], [11,12,13,14]]

def print_score(datas): # datas == list
    print("sum", sum(datas))       
    print("max", max(datas))
    print("min", min(datas))
    print("avg", sum(datas)/len(datas))
    print()

def analyze_list(datas):
        print("리스트 데이터 분석")
        for i1, d1 in enumerate(datas):
            print(f"{i1+1}번째 : ", end="")
            for i2, d2 in enumerate(d1):
                print(f"[{i2+1}]{d2} ", end="")
        print()
        print_score(d1)
        
data3 = {   "김인하" : [1,2]
            ,   "이인하" : [10,20,30,40,50,60,70]
            ,   "송인하" : [11,12,13,14]
            }

def analyze_dict(datas):
    print("딕셔너리 데이터 분석")
    for d1 in datas:     # !!!
        print(f"{d1} : ", end="")
        for i2, d3 in enumerate(datas[d1]):
            print(f"[{i2+1}]{d3} ", end="")
        print()
        print_score(datas[d1])

analyze_list(data2)
analyze_dict(data3)
# analyze_list(data3) data3은 딕셔너리라서 오류남

def analyze_score(datas):
    if isinstance(datas, list):
        analyze_list(datas)
    elif isinstance(datas, dict):
        analyze_dict(datas)
    else:
        print("분석 불가")

analyze_score(data2)
analyze_score(data3)

