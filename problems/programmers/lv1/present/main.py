def solution(friends, gifts):
    answer = 0

    n = len(friends)
    nums = dict()
    for i, f in enumerate(friends):
        nums[f] = i
    board = [[0] * n for _ in range(n)]
    for sender, receiver in gifts:
        s_num = nums[sender]
        r_num = nums[receiver]
        board[s_num][r_num] += 1
        board[r_num][s_num] -= 1
    

    return answer