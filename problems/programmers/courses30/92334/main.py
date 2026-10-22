def solution(id_list : list, report, k):
    answer = []

    l = len(id_list)
    reporters = {x : set() for x in id_list}

    for log in report:
        reporter, reported = log.split()
        reporters[reported].add(reporter)

    cnts = {x : 0 for x in id_list}
    for v in reporters.values():
        if len(v) >= k:
            for reporter in v:
                cnts[reporter] += 1
    for t in cnts.values():
        answer.append(t)

    return answer