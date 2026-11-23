def solution(nums):
    answer = -1
    pn = [True] * 3000
    pn[0] = pn[1] = False
    for i in range(2, 3000):
        if not pn[i]:
            continue
        for j in range(2*i, 3000, i):
            pn[j] = False
    l = len(nums)
    cnt = 0
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if pn[nums[i] + nums[j] + nums[k]]:
                    cnt += 1
    answer = cnt
    return answer