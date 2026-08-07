def solution(t, p):
    answer = 0
    
    l = len(p)
    p_num = int(p)
    for i in range(len(t) - l + 1):
        sub_t_num = int(t[i:i+l])
        answer += 1 if sub_t_num <= p_num else 0
        print(sub_t_num)

    return answer
