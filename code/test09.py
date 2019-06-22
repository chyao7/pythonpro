

num = int(input())
res = []

while num/2 != 0:
    if num%2 == 0:
        res.append("0")
    else:
        res.append("1")
    num = num//2

print(res.count("1"))