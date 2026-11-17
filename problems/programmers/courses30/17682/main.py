def solution(dartResult):
    answer = 0
    nums = []
    for i, x in enumerate(dartResult):
        if '0' <= x <= '9':
            if x == '0' and dartResult[i-1] == '1':
                nums[-1] = 10
            else:
                nums.append(int(x))
        else:
            if x == 'S':
                continue
            elif x == 'D':
                nums[-1] **= 2
            elif x == 'T':
                nums[-1] **= 3
            elif x == '*':
                nums[-1] *= 2
                if len(nums) > 1:
                    nums[-2] *= 2
            elif x == '#':
                nums[-1] *= -1
    answer = sum(nums)
    return answer