try:
    watermelon = int(input('kg: '))
except ValueError:
    print('invalid value')
else:
    if watermelon == 2:
        print("NO")
    elif watermelon % 2 == 0:
        print("YES")
    else:
        print("NO")
