first_side = int(input('1-st side: '))
second_side = int(input('2-nd side: '))
slab = int(input('slab: '))
first_side = first_side % slab
second_side = second_side % slab
tmp = first_side * second_side
print(tmp)