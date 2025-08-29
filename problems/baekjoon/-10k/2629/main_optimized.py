# 2629. 양팔저울
import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
beads = list(map(int, input().split()))

possible = {0}

for w in weights:
    new = set()
    for diff in possible:
        new.add(diff + w)
        new.add(abs(diff - w))
    possible |= new

for bead in beads:
    print("Y" if bead in possible else "N")