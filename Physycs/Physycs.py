a = []
b = int(input())
for item in range(b):
    str_score = input().split()
    int_score = list(map(int, str_score))
    a.append(int_score)
print()