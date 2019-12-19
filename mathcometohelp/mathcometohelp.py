import re
n = input()
n = re.split(r'\+', n)
n.sort()
output_string = ''
for item in  n:
    output_string += item+'+'
print(output_string[:-1])