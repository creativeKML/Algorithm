submitted = set()

for _ in range(28):
    submitted.add(int(input()))

all_students = set(range(1, 31))

missing = sorted(all_students - submitted)

print(missing[0])
print(missing[1])
