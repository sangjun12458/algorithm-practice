def solution(bandage, health, attacks):
    answer = 0

    for t, damage in attacks[:-1]:
        # 회복중인 경우에 대한 처리

        # 피해
        health -= damage

        # 다시 붕대 감기

        pass

    return answer