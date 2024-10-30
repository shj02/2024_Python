# week10_02.py
f = open(r"c:\202444040\sonhyeji02.txt", 'a')

scores = {'math':90, 'kor':100, 'eng':10}

while True:
    scores['math'] = int(input("math:"))
    scores['kor'] = int(input("kor:"))
    scores['eng'] = int(input("eng:"))

    data = ""
    for k, v in scores.items():
        if data:
            data += "|"
        data += (f"{k}, {v}")
    f.write(f"{data}\n")

    if "Y" == input("종료(Y):").upper():
        break
    
f.close()

'''
f = open(r"c:\202444040\sonhyeji01.txt", 'a')

scores = {}

while True:
    scores['math'] = int(input("math:"))
    scores['kor'] = int(input("kor:"))
    scores['eng'] = int(input("eng:"))

    for k, v in scores.items():
        f.write(f"{k}, {v}\n")

    if "Y" == input("종료(Y):").upper():
        break
    
f.close()

-

f = open(r"c:\202444040\sonhyeji01.txt", 'w')

scores = {'math':90, 'kor':100, 'eng':10}

for k, v in scores.items():
    f.write(f"{k}, {v}\n")

f.close()
'''
