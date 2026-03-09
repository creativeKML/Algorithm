N = int(input())

scores = list(map(int, input().split()))
avg = []

M = max(scores)

for score in scores:
    avg.append(score/M*100)
    
print(sum(avg)/N)