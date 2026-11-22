def solution(nums):
    answer = -1
    cnts = [0] * 3000
    for n in nums:
        cnts[n] += 1
    for _ in range(2):
        for n in nums:
            for i in range(3000):
                if cnts[i]:
                    cnts[i + n] += cnts[i]
    return answer