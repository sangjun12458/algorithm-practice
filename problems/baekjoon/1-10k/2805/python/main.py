import sys
input = sys.stdin.readline

n, m = map(int, input().split())
woods = list(map(int, input().split()))

start = 0
#end = woods[-1]
end = max(woods)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    # total = 0
    # for i in woods:
    #     if i > mid:
    #         total += (i - mid)
    total = sum(w - mid for w in woods if w > mid)

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)