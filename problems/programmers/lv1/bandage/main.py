def solution(bandage, health, attacks):
    answer = health
    # last_attack_time = attacks[-1][0]
    # for t in range(1, last_attack_time+1):
    #     pass

    for idx, (t, damage) in enumerate(attacks):

        # 다시 붕대 감기
        nt = attacks[idx+1][0]
        interval = nt - t
        health += interval * bandage[1]
        if interval >= bandage[0]:
            health += bandage[2]

        # 피해
        health -= damage
        if health <= 0:
            return -1

    return health