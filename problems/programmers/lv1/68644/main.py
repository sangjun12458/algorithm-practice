def solution(numbers):
    answer = []

    l = len(numbers)
    s = set()
    for i in range(l):
        x = numbers[i]
        for j in range(i+1, l):
            s.add(x + numbers[j])

    answer.extend(s)
    answer.sort()

    return answer