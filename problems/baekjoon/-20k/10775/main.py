# 10775. 공항

g = int(input().strip())
p = int(input().strip())

gates = [False] * (g + 1)

for i in range(1, p+1):
    gi = int(input().strip())
    docking = False
    for gate in range(gi, 0, -1):
        if not gates[gate]:
            gates[gate] = True
            docking = True
            break
    if not docking:
        print(gates.count(True))
        break
