inp = input().split()

m = int(inp[0])/100
kg = int(inp[1])
BMI = kg/(m**2)

print(int(BMI))

if BMI >= 25:
    print("Obesity")