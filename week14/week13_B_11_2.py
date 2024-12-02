# week13_B_11_2.py
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

    members = os.listdir(mypath)
    for member in members:
        member_fullname = os.path.join(mypath, member)

        if os.path.isfile(member_fullname):
            file_ext = os.path.splitext(member) # 111가1234 / .txt (ext)
            if len(file_ext) == 2 and file_ext[-1] == ".txt":
                number = file_ext[0].strip()
                cars[number] = []

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
                            cars[number].append({'in':intime, 'out':outtime})
                            
    if cars:
        for number, times in cars.items():
            print(f"{number}")
            for time in times:
                print(f"{time['in']}, {time['out']}", end="")
                print(f"{diff_seconds(time['in'], time['out']})")
    else:
        print("기존 데이터 없음")

        
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
            f.write(f"{intime}|{outtime}\n")
        else:
            f.write(f"{intime}|")
        
    for number, time in cars.items:
        print(f"{number}의 차량기록: ")
        for i, time in enumerate(times):
            print(f"  [{i+1}] in:{time['in']}, out:{time[out]}", end="")
            print(f" diff:{diff_seconds[time['in'], time['out']}")
            
        print(car["num"], car["in"], car["out"])
        print(diff_seconds(car['in'], car['out'])
