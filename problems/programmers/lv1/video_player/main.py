def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    def cal_tatal_minutes(t):
        return 60 * int(t[:2]) + int(t[3:])

    video_len_m = cal_tatal_minutes(video_len)
    pos_m = cal_tatal_minutes(pos)
    op_start_m = cal_tatal_minutes(op_start)
    op_end_m = cal_tatal_minutes(op_end)

    for command in commands:
        if op_start_m <= pos_m < op_end_m:
            pos_m = op_end_m
        if command == 'prev':
            pos_m = max(0, pos_m - 10)
        elif command == 'next':
            pos_m = min(video_len_m, pos_m + 10)
    if op_start_m <= pos_m < op_end_m:
        pos_m = op_end_m

    answer = f'{pos_m // 60:0>2}:{pos_m % 60:0>2}'

    return answer