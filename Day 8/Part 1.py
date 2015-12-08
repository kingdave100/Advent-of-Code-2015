input = f = open('input.txt', 'r').read()
input = input.split("\n")
totalChars = 0
stringLength = 0
for line in input:
    totalChars += len(line)
    stringLength += len(eval(line))
print totalChars - stringLength