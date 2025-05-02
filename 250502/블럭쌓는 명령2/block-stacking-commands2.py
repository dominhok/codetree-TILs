n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
answer = [0] * (n+1)

for i in range(k):
    s, e = commands[i]
    for i in range(s,e+1):
        answer[i] +=1

print(max(answer))