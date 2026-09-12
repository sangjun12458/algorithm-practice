def solution(numbers, hand):
    answer = ''

    pos_dict = dict()
    for i in range(3):
        for j in range(3):
            pos_dict[i * 3 + j + 1] = (i, j)
    pos_dict['*'] = (3, 0)
    pos_dict[0] = (3, 1)
    pos_dict['#'] = (3, 2)

    lh = '*'
    rh = '#'

    for n in numbers:
        left_turn = True
        if n in [3, 6, 9]:
            left_turn = False
        elif n in [2, 5, 8, 0]:
            lh_pos = pos_dict[lh]
            rh_pos = pos_dict[rh]
            n_pos = pos_dict[n]
            lh_d = abs(lh_pos[0] - n_pos[0]) + abs(lh_pos[1] - n_pos[1])
            rh_d = abs(rh_pos[0] - n_pos[0]) + abs(rh_pos[1] - n_pos[1])
            if lh_d > rh_d:
                left_turn = False
            elif lh_d == rh_d:
                if hand == 'right':
                    left_turn = False

        if left_turn:
            lh = n
            answer += 'L'
        else:
            rh = n
            answer += 'R'

    return answer