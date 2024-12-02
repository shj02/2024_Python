# week13_B_11_1.py

from datetime import datetime as dt
from week13_B_car import Car1 as Car
import os

dtformat = "%Y-%m-%d %H:%M:%S"

'''
def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.now()
    return (outtime - intime).total_seconds()
'''

if __name__ == "__main__":
    mydir = "c:\\car1_24000001"
    myfile = "list.txt"
    myfullfile = os.path.join(mydir, myfile)

    if not os.path.isdir(mydir):
        os.mkdir(mydir)

    cars = []

    # read
    if os.path.isfile(fullfile):
        with open(fullfile, 'r', encoding='utf-8') as f:
            for line in f:
                # print(line)
                split_datas = line.strip().split('|')
                if split_datas and len(split_datas) == 3:
                    number = split_datas[0].strip()
                    dt.strptime(split_datas[1].strip(), dtformat)
                    if split_datas[-1].strip():
                        dt.strptime(split_datas[-1].strip(), dtformat)
                    else:
                        outtime = None

                    # cars.append({"num":number, "in":intime, "outtime":outtime})
                    cars.append(Car(number, intime, outtime))
    if cars:
        print("복구한 정보입니다.")
        for car in cars:
            print(car["num"], car["in"], car["out"])
    else:
        print("기존 저장 데이터가 없습니다.")

    while True:
        number = input("차량번호:").strip()
        if not number:
            break

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

        # car = {"num": number, "in": intime, "out": outtime}
        car = Car(number, intime, outtime)
        cars.append(car)

    for car in cars:
        # print(car["num"], car["in"], car["out"])
        # print(diff_seconds(car["in"], car["out"]))
        print(car.number, car.intime, car.outtime)
        print(car.diff_seconds())

    with open(myfullfile, "w", encoding="utf-8") as f:
        for car in cars:
            # num = car["num"]
            num = car.number
            # intime = dt.strftime(car["in"], dtformat)
            intime = dt.strftime(car.intime, dtformat)
            # outtime = dt.strftime(car["out"], dtformat) if car["out"] else ""
            outtime = dt.strftime(car.outtime, dtformat) if car.outtime else ""
            f.write(f"{num}|{intime}|{outtime}\n")
