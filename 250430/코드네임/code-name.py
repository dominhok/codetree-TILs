MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class agent:
    def __init__(self, codename = "", score = 0):
        self.codename = codename
        self.score = score

agents = [agent() for _ in range(MAX_N)]

for i in range(MAX_N):
    agents[i].codename = codenames[i]
    agents[i].score = scores[i]

min_idx = 0

for i in range(MAX_N):
    if agents[min_idx].score > agents[i].score:
        min_idx = i


print(agents[min_idx].codename, agents[min_idx].score)