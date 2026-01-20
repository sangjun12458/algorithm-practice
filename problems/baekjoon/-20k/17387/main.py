# 17387. 선분 교차 2

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def cross(v1, v2):
    return v1[0]*v2[1]-v1[1]*v2[0]
def on_line(v1, v2, t):
    return (v1[0]<=t[0]<=v2[0] or v2[0]<=t[0]<=v1[0]) and \
           (v1[1]<=t[1]<=v2[1] or v2[1]<=t[1]<=v1[1])

v12 = (x2-x1, y2-y1)
v13 = (x3-x1, y3-y1)
v14 = (x4-x1, y4-y1)
c1 = cross(v12, v13)
c2 = cross(v12, v14)

v34 = (x4-x3, y4-y3)
v31 = (x1-x3, y1-y3)
v32 = (x2-x3, y2-y3)
c3 = cross(v34, v31)
c4 = cross(v34, v32)

if c1*c2 == 0 and c3*c4 == 0:
    if on_line((x1, y1), (x2, y2), (x3, y3)) or \
       on_line((x1, y1), (x2, y2), (x4, y4)) or \
       on_line((x3, y3), (x4, y4), (x1, y1)) or \
       on_line((x3, y3), (x4, y4), (x2, y2)):        
        print(1)
    else:
        print(0)
elif c1*c2 <= 0 and c3*c4 <= 0:
    print(1)
else:
    print(0)