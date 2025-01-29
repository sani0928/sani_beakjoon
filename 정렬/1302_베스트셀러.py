n = int(input())
count = [0] * n
books = [input() for _ in range(n)]
for i in books:
    count[books[i]] += 1

print(count)