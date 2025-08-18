import sys
input = sys.stdin.readline
# write = sys.stdout.write

n, m = map(int, input().split())
basket = [i for i in range(0, n + 1)]
# basket = list(range(i, n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    basket[a], basket[b] = basket[b], basket[a]
    # basket[a - 1], basket[b - 1] = basket[b - 1], basket[a - 1]

print(" ".join(map(str, basket[1:])))
# write(" ".join(map(str, basket)))