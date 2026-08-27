def solution(friends, gifts):
    answer = 0

    n = len(friends)
    nums = dict()
    for i, f in enumerate(friends):
        nums[f] = i
    board = [[0] * n for _ in range(n)]
    for gift in gifts:
        sender, receiver = gift.split(' ')
        s_num = nums[sender]
        r_num = nums[receiver]
        board[s_num][r_num] += 1
        board[r_num][s_num] -= 1
    
    #best_sender = -1
    # best_score = -100
    # for i in range(n):
    #     s_total = sum(board[i])
    #     r_total = sum([board[j][i] for j in range(n)])
    #     score = s_total - r_total
    #     if score > best_score:
    #         #best_sender = i
    #         best_score = score
    # answer = best_score

    for i in range(n):
        for j in range(i+1, n):
            score = board[i][j]
            if score > 0:
                board[i][i] += 1
            elif score < 0:
                board[j][j] += 1
            else:
                i_total = sum(board[i])
                j_total = sum(board[j])
                if i_total > j_total:
                    board[i][i] += 1
                elif i_total < j_total:
                    board[j][j] += 1

    answer = -100
    for i in range(n):
        answer = max(answer, board[i][i])

    return answer