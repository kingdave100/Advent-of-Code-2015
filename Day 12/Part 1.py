import re
input = f = open('input.txt', 'r').read()
print eval('+'.join(re.findall(r'\-?\d+', input)))