n = int(input())
n_2 = []
# Please write your code here.

if n == 0:
    print('0')

while n != 0:
    a = n % 2
    n_2.append(a)
    n //= 2

for i in range(len(n_2)):
    print(n_2[-(i+1)], end='') 