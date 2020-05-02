count = 0
matrix = []
for item in range(5):
    tmp = input().split()
    matrix.append(tmp)
if '1' in matrix[0]:
    count += 2
elif '1' in matrix[1]:
    count += 1
elif '1' in matrix[2]:
    pass
elif '1' in matrix[3]:
    count += 1
elif '1' in matrix[4]:
    count += 2
