secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class agent:
    def __init__(self, code, meet, time):
        self.code = code
        self.meet = meet
        self.time = time

agent1 = agent(secret_code, meeting_point, time)

print("secret code :", agent1.code)
print("meeting point :", agent1.meet)
print("time :", agent1.time)
