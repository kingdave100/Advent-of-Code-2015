import re
password = 'hxcaabcc'

def validity(s):
    for c in ['i', 'l', 'o']:
        if c in s:
            return False

    for i in range(0, len(s)-2):
        if ord(s[i]) == ord(s[i+1]) - 1 and ord(s[i+1]) == ord(s[i+2]) - 1:
            break
    else:
        return False

    if len(re.findall(r'(.)\1+', s)) < 2:
        return False

    return True

def increment(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    try:
        return s[0:-1] + alpha[alpha.index(s[-1]) + 1]
    except IndexError:
        return increment(s[0:-1]) + 'a'

while True:
    password = increment(password)
    if validity(password):
        print password
        break