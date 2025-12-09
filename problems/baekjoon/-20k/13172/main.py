# 13172. Σ
import sys
input = sys.stdin.readline
MOD = 1_000_000_007

M = int(input())

def modulo_inverse():
    return

ans = 0
for _ in range(M):
    N, S = map(int, input().split())
    ans += modulo_inverse(N, S)