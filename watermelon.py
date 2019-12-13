try:
    watermelon = int(input('kg: '))
except ValueError:
    print('invalid value')
else:
    if watermelon % 2 == 0:
        print('yes')
    else:
        print('no')