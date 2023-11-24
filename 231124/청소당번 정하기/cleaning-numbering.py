n = int(input())
cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in range(0,n+1):
    if(i % 12 == 0):
        cnt1 += 0
    else:
        if(i % 3 == 0):
                cnt2 += 1
        else:
            if(i % 2 == 0):
                cnt3 += 1


print(cnt3, end = " ")
print(cnt2, end = " ")
print(cnt1, end = " ")