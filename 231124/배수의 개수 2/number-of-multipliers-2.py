arr = []
cnt = 0

for i in range(0,10):
    arr.append(int(input()))

for i in range(0,10):
    if ((arr[i] % 2) == 1) :
        cnt+=1

print(cnt)