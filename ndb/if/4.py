a = input()
b = input()

ia = int(a.split()[0])
ib = int(b.split()[0])

if ia > 0 and ib > 0:
    print("1")
elif ia > 0 and ib < 0:
    print("4")
elif ia < 0 and ib > 0:
    print("2")
else:
    print("3")


