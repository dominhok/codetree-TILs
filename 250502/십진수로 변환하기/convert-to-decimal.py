binary = input()
answer = 0
val = 1
# Please write your code here.

for x in binary[::-1]:
    answer += int(x) * val
    val *=2

print(answer)