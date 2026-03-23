A, B = input().split()

cA = int(A[::-1])
cB = int(B[::-1])

if cA > cB :
	print(cA)
else :
	print(cB)