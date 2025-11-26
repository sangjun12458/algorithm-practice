a = [0] * 4

def func(b):
    b[2] = 999

func(a)

print(a)