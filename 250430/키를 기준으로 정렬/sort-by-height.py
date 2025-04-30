n = int(input())
name = []
height = []
weight = []
humans = []

class human:
    def __init__(self, name ,height, weight):
        self.name = name
        self.height = height
        self.weight = weight

for _ in range(n):
    n_i, h_i, w_i = input().split()
    humans.append(human(n_i, int(h_i), int(w_i)))

# Please write your code here.
humans.sort(key = lambda x: x.height)

for human in humans:
    print(human.name, human.height, human.weight)