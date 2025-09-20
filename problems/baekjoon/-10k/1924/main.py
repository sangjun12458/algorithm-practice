# 1924. 2007년
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())
days = 0
for month in range(1, x):
    if month == 2:
        days += 28
    elif month in [4, 6, 9, 11]:
        days += 30
    else:
        days += 31
print(week[(days + y) % 7])