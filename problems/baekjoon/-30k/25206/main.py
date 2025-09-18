# 25206. 너의 평점은
import sys
input = sys.stdin.readline

grades = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
          'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
          'F': 0}

credits = 0
total = 0
for _ in range(20):
    _, credit, grade = input().split()

    if grade == 'P':
        continue

    credits += float(credit)
    total += float(credit) * grades[grade]

if credits == 0:
    print(0)
else:
    print(total / credits)