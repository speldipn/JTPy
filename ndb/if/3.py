a = input()
ia = int(a)

if ia % 4 == 0 and (ia % 100 != 0 or ia % 400 == 0):
    print("1")
else:
    print("0")
