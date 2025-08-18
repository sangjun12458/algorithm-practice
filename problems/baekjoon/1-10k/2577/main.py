a = int(input())
b = int(input())
c = int(input())
x = a * b * c
cnt = [0] * 10
while x > 0:
    cnt[x % 10] += 1
    x = x // 10
for i in cnt:
    print(i)

### 메모리 사용량 극도로 최적화
'''
a = int(input()) * int(input()) * int(input())
for i in range(10):
    print(str(a).count(str(i)))
'''
### 속도 극도로 최적화
'''
a = int(input()) * int(input()) * int(input())
cnt = [0] * 10
while a:
    cnt[a % 10] += 1
    a //= 10
print(*cnt, sep='\n')
'''