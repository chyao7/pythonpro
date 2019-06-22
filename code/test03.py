

"""
180 = 2*2*3*3*5
"""
num = int(input())
res = []
for i in range(2,num):
    while num%i ==0:
        num = num/i
        res.append(i)

print(" ".join(map(str,res))+" " if res else str(num)+" ")
