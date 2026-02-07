price = int(input())
num = int(input())

total = 0

for _ in range(num):
    a, b = map(int, input().split())
    total += a*b
    
if total == price:
    print("Yes")
else:
    print("No")