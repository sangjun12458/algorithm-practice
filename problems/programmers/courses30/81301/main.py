def solution(s: str):
    answer = 0

    words = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    digits = [i for i in range(10)]

    for i in range(10):
        word = words[i]
        while word in s:
            idx = s.index(word)
            

    return answer