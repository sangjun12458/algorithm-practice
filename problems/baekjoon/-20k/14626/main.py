# 14626. ISBN
isbn = list(input().strip())
idx = isbn.index('*')
for i in range(10):
    checksum = 0
    isbn[idx] = f'{i}'
    for j in range(len(isbn)-1):
        checksum += int(isbn[j]) if j % 2 == 0 else 3 * int(isbn[j])
    checksum = int(isbn[-1]) + (checksum % 10)
    if checksum == 0 or checksum == 10:
        print(isbn[idx])
        exit()