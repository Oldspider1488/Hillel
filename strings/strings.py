import re
string = input().lower()
string = re.sub('[aoyeui]', '.', string)

out_string = "."
for t in string:
    out_string += t + '.'
print(out_string[:-1])

