# 27433. 팩토리얼 2
n = int(input().strip())

def facto(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * facto(x - 1)
    
print(facto(n))