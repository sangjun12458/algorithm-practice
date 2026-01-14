# 17387. 선분 교차 2

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

r1 = (y1-y2)/(x1-x2)
r2 = (y3-y4)/(x3-x4)

if r1 == r2:
    if y1-r1*x1 == y3-r2*x3:
        if x1 <= x3 <= x2 or x2 <= x3 <= x1:
            print(1)
        elif x1 <= x4 <= x2 or x2 <= x4 <= x1:
            print(1)
        elif x3 <= x1 <= x4 or x4 <= x1 <= x3:
            print(1)
        elif x3 <= x2 <= x4 or x4 <= x2 <= x3:
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    x = (r1*x1 - r2*x3 - y1 + y3)/(r1-r2)
    y = r1*(x-x1)+y1

    print(x, y)

    if x1 <= x <= x2 or x2 <= x <= x1:
        if y1 <= y <= y2 or y2 <= y <= y1:
            if x3 <= x <= x4 or x4 <= x <= x3:
                if y3 <= y <= y4 or y4 <= y <= y3:
                    print(1)
                else:
                    print(0)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)