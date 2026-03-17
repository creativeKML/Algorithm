T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    
    result = ""
    
    for w in S:
        result += w * R
        
    print(result)