

s = input().split(";")

dot =[0,0]

for i in s:
    try:
        if i[0]=="A" :
            dot[0] -= int(i[1:])

        if i[0]=="D":
            dot[0] += int(i[1:])

        if i[0]=="S":
            dot[1] -= int(i[1:])

        if i[0]=="W":
            dot[1] += int(i[1:])
    except:
        pass

print(",".join(map(str,dot)))