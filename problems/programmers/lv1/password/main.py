def solution(s, skip, index):
    answer = ''

    skip_number = [ord(x) - ord('a') for x in skip]
    shifted = [0] * 26

    for i in range(26):
        shifted_number = i
        for _ in range(index):
            shifted_number = (shifted_number + 1) % 26
            while shifted_number in skip_number:
                  shifted_number = (shifted_number + 1) % 26
        shifted[i] = shifted_number
 
    for x in s:
        answer += chr(ord('a') + shifted[ord(x) - ord('a')])
 
    return answer