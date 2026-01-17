# 2754. 학점계산

d = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0,
     '+': 0.3, '0': 0.0, '-': -0.3}

grade = input().strip()
ans = 0.0 if grade == 'F' else d[grade[0]] + d[grade[1]]

print(ans)