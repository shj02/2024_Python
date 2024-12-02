# week13_B_08_2.py
# id: 202444040
# name: sonhyeji

from datetime import datetime as dt

dtformat = "%Y-%m-%d %H:%M:%S"
mypath = "c:\\car2_202444040"

def diff_seconds(intime,outtime):
    if not outtime:
        outtime = dt.now()    
    return (outtime - intime).total_seconds()

if __name__ = "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
        
    cars = {}
    while True:
        number = input("차량번호:").strip()
        if not number:
            break

        if not number in cars.keys():
            cars[number] = []
        else:
            for time in cars[number]:
                if time["out"] == None:
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

        car = {'in':intime, 'out':outtime}
        cars[number].append(car)

    fullfile = os.path.join(mypath, number+'txt')
    with open(fullfile, 'a', encoding='utf-8') as f:
        intime = dt.strftime(intime, dtformat)
        if outtime:
            outtime = dt.strftime(outtime, dtformat)
            f.write(f"{number}|{intime}|{outtime}\n")
        else:
            f.write(f"{number}|{intime}|")
        
    for number, time in cars.items:
        print(f"{number}의 차량기록: ")
        for i, time in enumerate(times):
            print(f"  [{i+1}] in:{time['in']}, out:{time[out]}", end="")
            print(f" diff:{diff_seconds[time['in'], time['out']}")
            
        print(car["num"], car["in"], car["out"])
        print(diff_seconds(car['in'], car['out'])
