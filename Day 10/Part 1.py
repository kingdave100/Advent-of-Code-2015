input = "1113122113"
def lookAndSay(num):
    output = ""
    repeat = num[0]
    number = num[1:]+" "
    times = 1

    for i in number:
        if i != repeat:
            output += str(times)+repeat
            times = 1
            repeat = i
        else:
            times += 1
    return output

for i in range(40):
    input = lookAndSay(input)
print len(input)