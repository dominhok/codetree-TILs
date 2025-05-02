n = int(input())
segments = [tuple(map(lambda x: int(x)+100, input().split())) for _ in range(n)]
answer = [0] * 201
# Please write your code here.
for i in range(n):
    s,e = segments[i]
    for x in range(s,e):
        answer[x] += 1

print(max(answer))
    