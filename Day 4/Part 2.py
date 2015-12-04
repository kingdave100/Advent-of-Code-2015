import md5
x = 0
while True:
    x += 1
    m = md5.new()
    m.update("yzbqklnj"+str(x))
    if m.hexdigest()[0:6] == "000000":
        print "yzbqklnj"+str(x)
        print m.hexdigest()
        print x
        break