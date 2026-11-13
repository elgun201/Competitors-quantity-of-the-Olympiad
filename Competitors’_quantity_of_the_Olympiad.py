import sys

data = sys.stdin.read().split()
if len(data) >= 4:
    k = int(data[0])
    m = int(data[1])
    n = int(data[2])
    d = int(data[3])

    asagi = (k * m * n) - (m * n) - (k * n) - (k * m)

    if asagi <= 0:
        print(-1)
    else:
        yuxari = d * k * m * n
        if yuxari % asagi == 0:
            print(yuxari // asagi)
        else:
            print(-1)
