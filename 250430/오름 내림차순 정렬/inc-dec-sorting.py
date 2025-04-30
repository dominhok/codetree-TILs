n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
sorted1 = sorted(nums)
sorted2 = sorted(nums, reverse = True)

print(' '.join(map(str, sorted1)))
print(' '.join(map(str, sorted2)))

