# week13_B_11_4.py
# id: 202444040
# name: sonhyeji

from week13_B_car import Car2 as Car
from week13_B_car import TimeStamp
from datetime import datetime as dt
import datetime
import os
import random

dtformat = "%Y-%m-%d %H:%M:%S"
mypath = "c:\\car2_202444040"

def gen_korean_car_plate():
    korean_characters = "허하호"
    # 10가1111 111가1111

    numold = f"{random.randrange(10, 99, 1)}" # 10부터 99되기 전까지 1칸씩 랜덤 정수 생성
    numnew = f"{random.randint(100, 999)}" # 100부터 999까지 랜덤 정수 생성 

    front_number = random.choice([numold, numnew]) # 추출
    kor_char = random.choice(korean_characters)
    rear_number = f"{random.randint(1000, 9999)}"

    return f"{front_number}{kor_char}{rear_number}"

def generate_intime():
    return dt.now() - datetime.timedelta(hours=random.randint(0, 5),
                                  minutes=random.randint(0, 60))

def generate_outtime():
    return dt.now() + datetime.timedelta(hours=random.randint(1, 48),
                                  minutes=random.randint(0, 60))    

if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
        
    cars = [] # Car2의 인스턴스가 들어감

    members = os.listdir(mypath)
    for member in members:
        member_fullname = os.path.join(mypath, member)

        if os.path.isfile(member_fullname):
            file_ext = os.path.splitext(member) # 111가1234 / .txt (ext)
            if len(file_ext) == 2 and file_ext[-1] == ".txt":
                number = file_ext[0].strip()
                # cars[number] = []
                car = Car(number)

                with open(member_fullname, 'r', encoding='utf-8') as f:
                    for line in f:
                        split_datas = line.strip().split('|')
                        if split_datas and len(split_datas) == 2:
                            intime = dt.strptime(split_datas[0].strip(), dtformat)
                            if split_datas[1].strip():
                                outtime = dt.strptime(split_datas[1].strip(), dtformat)
                            else:
                                outtime = None

                            # 밑에 있는 내용을 dict 대신 TimeStamp로 변경해볼 것
                            # cars[number].append({'in':intime, 'out':outtime})
                            car.add_timestamp(intime, outtime)

                if car.history:
                    cars.append(car)
                            
    if cars:
        for car in cars:
            print(f"{car.number}")
            for time in car.history:
                print(f"{time.intime}, {time.outtime}", end="")
                print(f"{time.diff_seconds()}")
    else:
        print("기존 데이터 없음")

        
    while True:
        number = input("차량번호:").strip()
        if not number:
            break

        search_car = [car for car in cars if car.number == number]

        if not search_car: # not number in cars.keys():
            # cars[number] = []
            car = Car(number)
            cars.append(car)
        else:
            for time in search_car[0].history: # time in cars[number]:
                if is_not_exit():              # time["out"] == None:
                    print("출차하지 않은 차량입니다.")
                    continue

        while True:
            try:
                intime = input("입차시간:").strip()
                if intime:
                    intime = dt.strptime(intime, dtformat)
                    break
            except:
                pass
            
            
        while True:
            try:
                outtime = input("출차시간:").strip()
                if not outtime:
                    outtime = None
                    break
                outtime = dt.strptime(outtime, dtformat)
                break
            except:
                pass

        car.add_timestamp(intime, outtime)
        # car = {'in':intime, 'out':outtime}
        # cars[number].append(car)
                
    fullfile = os.path.join(mypath, number + 'txt')
    with open(fullfile, 'a', encoding='utf-8') as f:
        intime = dt.strftime(intime, dtformat)
        if outtime:
            outtime = dt.strftime(outtime, dtformat)
            f.write(f"{intime}|{outtime}\n")
        else:
            f.write(f"{intime}|")
        
    for car in cars: # number, time in cars.items:
        print(f"{car.number}의 차량기록: ") # {number}
        for i, time in enumerate(car.history): # enumerate(times)
            print(f"  [{i+1}] in:{time.intime}, out:{time.outtime}", end="")
            print(f" diff:{time.diff_seconds()}")
            
        print(car["num"], car["in"], car["out"])
        print(diff_seconds(car['in'], car['out']))
