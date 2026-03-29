# 19238. 스타트 택시

N, M, gas = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(int, input().split()))
customer = [list(map(int, input().split())) for _ in range(M)]

for _ in range(M):
    # 택시로부터 최단거리 승객 찾기 + 찾을 수 없으면 종료
    
    # 출발지에서 목적지까지 최단거리 + 가지 못하거나 연료가 없으면 종료
    # 연료 충전 
    pass