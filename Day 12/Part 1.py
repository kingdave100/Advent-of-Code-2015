import re
input = f = open('input.txt', 'r').read()
print eval('+'.join(c for c in input if c.isdigit() or c == "-"))

print '+'.join(re.findall(r'\-?\d+', input))
print eval('+'.join(re.findall(r'\-?\d+', input)))