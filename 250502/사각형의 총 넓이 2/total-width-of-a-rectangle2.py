n = int(input())
cnt = 0
rect = [[0 for i in range(210)] for i in range(210)]

# Please write your code here.

for _ in range(n):
    x1, y1, x2, y2 = map(lambda x: int(x) + 100, input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            rect[j][k] = 1


for h in range(210):
    for j in range(210):
        if rect[h][j] == 1:
            cnt += 1

print(cnt)