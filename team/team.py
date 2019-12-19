count = 0
task = int(input())
for item in range(task):
    str_score = input().split()
    int_score = list(map(int, str_score))
    if sum(int_score) > 1:
        count += 1

print(count)