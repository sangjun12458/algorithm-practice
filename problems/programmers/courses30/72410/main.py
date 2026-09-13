# new name recommandation

def solution(new_id : str):
    answer = ''

    # 1. uppercase to lowercase
    new_id = new_id.lower()
    # 2. proper character refine
    temp = ''
    for c in new_id:
        if 'a' <= c <= 'z' or 0 <= c <= 9 or c in ['-', '_', '.']:
            temp.append(c)
    # 3. unique full stop
    
    # 4. 
    # 5.
    # 6.
    # 7.

    return answer