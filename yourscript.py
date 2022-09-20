import sys

count = 0
while True:
    buff = sys.stdin.readline()
    # print(buff)
    buff  = buff.split('","')
    # print(buff)
    try:
        # print(int(float(buff[2])))
        if int(float(buff[2])) > 200:
            count+=1
            print(f"Index {count}")
            if count == 5:
                print(f"End task.")
                break
    except (IndexError, ValueError):
        continue
    

 