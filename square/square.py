a, b, c = map(int, input().split())
a = (a + c - 1) // c
b = (b + c - 1) // c
print(a * b)