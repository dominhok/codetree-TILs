class student:
    def __init__(self,name,a,b,c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c


students = []

n = int(input())

for _ in range(n):
    name,a,b,c = input().split()
    students.append(student(name,int(a),int(b),int(c)))


students.sort(key=lambda x: x.a + x.b + x.c)

for student in students:
    print(student.name, student.a, student.b, student.c)

# Please write your code here.