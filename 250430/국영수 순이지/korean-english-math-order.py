n = int(input())
name = []
korean = []
english = []
math = []
students = []

class student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = int(korean)
        self.english = int(english)
        self.math = int(math)

for _ in range(n):
    name,korean,english,math = input().split()
    students.append(student(name,korean,english,math))
# Please write your code here.

students.sort(key = lambda x: (-x.korean, -x.english , -x.math))

for student in students:
    print(student.name, student.korean, student.english, student.math)