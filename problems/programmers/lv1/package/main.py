
def solution(n, w, num):
    answer = 0
    num -= 1
    
    # 전체 택배의 높이
    sh1 = n // (2*w)
    r = n % (2*w)
    sh2 = r // w
    r %= w
    heights = [2 * sh1 + sh2] * w
    if sh2:
        for i in range(-1, -1-r, -1):
            heights[i] += 1
    else:
        for i in range(r):
            heights[i] += 1
    #height = 2 * sh1 + sh2

    # 원하는 택배의 높이
    num_sh1 = num // (2*w)
    num_r = num % (2*w)
    num_sh2 = num_r // w
    num_r %= w
    num_height = 2 * num_sh1 + num_sh2

    # 빼낼 상자 개수 계산
    if num_sh2:
        answer = heights[w-1-num_r] - num_height
    else: 
        answer = heights[num_r] - num_height
    # if sh2 ^ num_sh2:
    #     answer -= 1 if r + num_r <= w else 0
    # else:
    #     answer -= 1 if r < num_r else 0
    return answer