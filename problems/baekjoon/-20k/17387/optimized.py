# 17387. 선분 교차 2

def ccw(x1, y1, x2, y2, x3, y3):
    v = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    if v > 0:
        return 1
    elif v < 0:
        return -1
    else:
        return 0
    
def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    ab_c = ccw(x1, y1, x2, y2, x3, y3)
    ab_d = ccw(x1, y1, x2, y2, x4, y4)
    cd_a = ccw(x3, y3, x4, y4, x1, y1)
    cd_b = ccw(x3, y3, x4, y4, x2, y2)

    if ab_c == 0 and ab_d == 0:
        return (min(x1, x2) <= max(x3, x4) and
                min(x3, x4) <= max(x1, x2) and
                min(y1, y2) <= max(y3, y4) and
                min(y3, y4) <= max(y1, y2))
    
    return ab_c * ab_d <= 0 and cd_a * cd_b <= 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

print(1 if is_intersect(x1, y1, x2, y2, x3, y3, x4, y4) else 0)