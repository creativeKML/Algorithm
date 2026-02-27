N, M = map(int, input().split())

# 바구니 생성
basket = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    
    # i-1부터 j까지 뒤집기
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)