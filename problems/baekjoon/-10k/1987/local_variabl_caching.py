import time

# 전역 변수
global_list = [1] * 100

def test_global_access():
    s = 0
    for _ in range(30_000_000):  # 3천만 번
        s += global_list[0]
    return s

def test_local_caching():
    s = 0
    local_list = global_list  # 지역 변수로 캐싱
    for _ in range(30_000_000):
        s += local_list[0]
    return s


# === 시간 측정 ===

start = time.time()
test_global_access()
end = time.time()
print(f"[전역 접근] 걸린 시간: {end - start:.4f}초")

start = time.time()
test_local_caching()
end = time.time()
print(f"[지역 캐싱] 걸린 시간: {end - start:.4f}초")
