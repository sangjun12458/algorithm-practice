document = input()
word = input()

count = 0
i = 0

while i <= len(document) - len(word):
    if document[i:i+len(word)] == word:
        count += 1
        i += len(word)  # 겹치지 않게 점프
    else:
        i += 1

print(count)
