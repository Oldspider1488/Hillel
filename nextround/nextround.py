count = 0
n, k = map(int, input().split())
str_score = input().split()
int_score = list(map(int, str_score))
for item in int_score:
    if item >= int_score[k-1] and item > 0:
        count += 1
print(count)