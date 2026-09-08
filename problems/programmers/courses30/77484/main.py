# 로또의 최고 순위와 최저 순위

def solution(lottos : list, win_nums : list):
    answer = []

    cnt = 0
    for x in lottos:
        for y in win_nums:
            if x == y:
                cnt += 1

    best = cnt + lottos.count(0)
    worst = cnt
    answer.append(7 - best if best >= 2 else 6)
    answer.append(7 - worst if worst >= 2 else 6)
 
    return answer