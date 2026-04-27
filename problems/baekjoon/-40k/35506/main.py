# 35506. Good Bye, 별 찍기!

N = int(input())
answer_list = [''] * 2*N

def print_diag(upper:bool=True, reverse:bool=False):
    start = 0 if upper else N
    for i in range(start, start+N):
        if not reverse:
            s = ' '*(N-i-1) + '*' + ' '*i
        else:
            s = ' '*i + '*' + ' '*(N-i-1)
            print(s)
        print(i, s)
        answer_list[i] += s

def print_empty(upper:bool=True, width:int=1):
    start = 0 if upper else N
    for i in range(start, start+N):
        answer_list[i] += ' '*width

print_empty(width=N)
print_diag()
print_empty()
print_diag()
print_empty()
print_diag(reverse=True)
print_diag(False)
# print_empty(False, N)
# print_diag(False)
# print_empty(False)
# print_diag(False, True)

for row in answer_list:
    print(row)
