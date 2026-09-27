# [PCCE 기출문제] 10번 / 데이터 분석

def solution(data, ext, val_ext, sort_by):
    answer = []

    key_index = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}

    for idx, (code, date, maximum, remain) in enumerate(data):
        if data[idx][key_index[ext]] < val_ext:
            answer.append([code, date, maximum, remain])
        
    answer.sort(key=lambda x: x[key_index[sort_by]])

    return answer