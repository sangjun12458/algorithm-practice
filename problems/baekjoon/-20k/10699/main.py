# 10699. 오늘 날짜
import time
t = time.localtime()
print(f'{t.tm_year}-{t.tm_mon:02d}-{t.tm_mday:02d}')
# from datetime import date
# print(date.today())