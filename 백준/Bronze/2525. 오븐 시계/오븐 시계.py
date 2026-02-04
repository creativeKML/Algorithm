H, M = map(int, input().split())
T = int(input())

total_minutes = H * 60 + M + T

H = (total_minutes // 60) % 24
M = total_minutes % 60

print(H, M)
