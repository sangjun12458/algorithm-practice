# 13172. Σ
import sys
input = sys.stdin.readline
MOD = 1_000_000_007

def modinv(a):
    # a^(MOD-2) % MOD  (Fermat’s little theorem)
    return pow(a, MOD - 2, MOD)

M = int(input())
ans = 0

for _ in range(M):
    N, S = map(int, input().split())
    ans = (ans + S * modinv(N)) % MOD

print(ans)