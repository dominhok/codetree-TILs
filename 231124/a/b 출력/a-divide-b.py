inp = input().split()

a = int(inp[0])
b = int(inp[1])
c = a // b
d = a % b
a = d * 10

print(c, end = ".")

for i in range(20):
    c = a // b
    d = a % b

    print(c, end = "")
     
    a = d * 10