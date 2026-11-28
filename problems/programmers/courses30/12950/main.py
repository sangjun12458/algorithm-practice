def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        r = []
        for x, y in zip(a, b):
            r.append(x + y)
        answer.append(r)
    return answe