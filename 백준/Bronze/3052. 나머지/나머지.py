n = []

for i in range(10):
    num = int(input())
    n.append(num % 42)
    
print(len(set(n)))