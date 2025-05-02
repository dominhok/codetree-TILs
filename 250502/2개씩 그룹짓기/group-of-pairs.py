n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.


asc = sorted(nums)
dsc = sorted(nums, reverse = True)


min_max = []
for i in range(len(nums)):
    min_max.append(asc[i]+dsc[i])

min_max.sort(reverse = True)
print(min_max[0])

