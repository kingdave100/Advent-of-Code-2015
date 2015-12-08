input = f = open('input.txt', 'r').read()
input = input.split("\n")
total = 0
for line in input:
    total += line.count('\\') + line.count('"') + 2
print total