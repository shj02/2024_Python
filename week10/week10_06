# week10_06.py

class Score:    # 자료 구조 생성
    def __init__(self, kor, eng, mat):     # 초기화
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def average(self):  # method
        return (self.kor+self.eng+self.mat) / 3

scores3 = Score(10, 20, 30)
print(scores3.kor, scores3.eng, scores3.mat)
print(scores3.average())

scores3.kor = 100
print(scores3.kor, scores3.eng, scores3.mat)
print(scores3.average())


def average_list(datas):    # function
    return sum(datas) / len(datas)


def average_dict(datas):
    return sum(datas.values()) / len(datas)


scores1 = [10, 20, 30]
scores2 = {"국어":10, "영어":20, "수학":30}

print(average_list(scores1))
print(average_dict(scores2))
