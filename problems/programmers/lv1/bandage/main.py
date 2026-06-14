def solution(bandage, health, attacks):
    answer = 0

    for idx, t, damage in enumerate(attacks[:-1]):
        # 피해
        health -= damage

        if health <= 0:
            return -1

        # 다시 붕대 감기
        nt = attacks[idx+1][0]
        interval = nt - t
        health += interval * bandage[1]
        if interval >= bandage[0]:
            health += bandage[2]

    return answer