def solution(s):
    answer = []

    last_poses = [-1] * 26
    for cur_pos, ch in enumerate(s):
        idx = ord(ch) - ord('a')
        last_pos = last_poses[idx]
        if last_pos == -1:
            answer.append(-1)
        else:
            answer.append(cur_pos - last_pos)
        last_poses[idx] = cur_pos

    return answer