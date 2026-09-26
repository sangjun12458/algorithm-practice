# [PCCE 기출문제] 10번 / 데이터 분석

def solution(data, ext, val_ext, sort_by):
    answer = []

    for idx, (code, date, maximum, remain) in enumerate(data):
        criteria_num = 0
        if ext == 'code':
            criteria_num = 0
        elif ext == 'date':
            criteria_num = 1
        elif ext == 'maximum':
            criteria_num = 2
        elif ext == 'remain':
            criteria_num = 3
        if data[idx][criteria_num] < val_ext:
            answer.append([code, date, maximum, remain])

    answer.sort(key=lambda x: x[criteria_num], reverse=True)

    return answer