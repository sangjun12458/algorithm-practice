def solution(schedules, timelogs, startday):
    answer = 0

    for idx, s in enumerate(schedules):
        target_time = s // 100 * 60 + s % 100
        for day in range(7):
            today = (startday + day) % 7
            if today in [6, 0]: continue
            log = timelogs[idx][day]
            today_time = log // 100 * 60 + log % 100
            



    return answer