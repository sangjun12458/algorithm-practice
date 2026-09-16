# new name recommandation

def solution(new_id : str):
    answer = ''

    # 1. 
    new_id = new_id.lower()
    # 2. 
    temp = ''
    prev = ''
    for c in new_id:
        if 'a' <= c <= 'z' or '0' <= c <= '9' or c in ['-', '_', '.']:
            if prev != '.' or c != '.':
                temp += c
            prev = c            
    new_id = temp
    # 4. 
    if new_id != '' and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id != '' and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5.
    if new_id == '':
        new_id = 'a'
    # 6.
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # 7.
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3-len(new_id))

    answer = new_id
    return answer
