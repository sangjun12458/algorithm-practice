def solution(bandage, health, attacks):
    max_health = health
    pt = 0
    
    for idx, (t, damage) in enumerate(attacks):
        # 회복
        interval = t - pt - 1
        health += interval * bandage[1]
        health += interval // bandage[0] * bandage[2]
        health = min(health, max_health)

        # 피해
        health -= damage
        if health <= 0:
            break

        print(interval, bandage[1], health)
        pt = attacks[idx][0]

    return health if health > 0 else -1
