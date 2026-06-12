def solution(bandage, health, attacks):
    answer = 0

    for idx, t, damage in enumerate(attacks[:-1]):
        # 회복중인 경우에 대한 처리

        # 피해
        health -= damage

        # 다시 붕대 감기
        nt = attacks[idx+1][0]
        interval = nt - t
        health += interval

        pass

    return answer