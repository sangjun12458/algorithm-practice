def solution(array, commands):
    answer = []

    for i, j, k in commands:
        sub_arr = array[i-1:j]
        sub_arr.sort()
        answer.append(sub_arr[k-1])

    return answer