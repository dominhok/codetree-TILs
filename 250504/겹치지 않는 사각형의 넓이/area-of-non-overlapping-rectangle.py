cnt = 0
rect = [[0 for i in range(2100)] for i in range(2100)]

# Please write your code here.

for i in range(3):
    x1, y1, x2, y2 = map(lambda x: int(x) + 1000, input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            if i == 2:
                rect[j][k] = 2
            else:
                rect[j][k] = 1


for h in range(2100):
    for j in range(2100):
        if rect[h][j] == 1:
            cnt += 1

print(cnt)



    