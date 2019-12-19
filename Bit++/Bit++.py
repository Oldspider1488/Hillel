count = 0
number = int(input())
for item in range(number):
    tmp = input()
    if '++' in tmp:
        count += 1
    else:
        count -= 1
print(count)