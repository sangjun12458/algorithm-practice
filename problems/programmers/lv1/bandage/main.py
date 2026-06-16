def solution(bandage, health, attacks):
    max_health = health
    # last_attack_time = attacks[-1][0]
    # for t in range(1, last_attack_time+1):
    #     pass
    pt = 0
    for idx, (t, damage) in enumerate(attacks):
        # 회복
        interval = t - pt
        health += interval * bandage[1]
        health += interval % bandage[0] * bandage[2]
        health = min(health, max_health)

        # 피해
        health -= damage
        if health <= 0:
            break

        pt = attacks[idx][0]

    return health if health > 0 else -1