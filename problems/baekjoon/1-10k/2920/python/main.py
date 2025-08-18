import sys
input = sys.stdin.readline

# seq = "".join(input().split())
seq = list(map(int, input().split()))

# if seq == "12345678":
#     print("ascending")
# elif seq == "87654321":
#     print("descending")
# else:
#     print("mixed")
if seq == list(range(1, 9)):
    print("ascending")
elif seq == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")