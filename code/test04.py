"""
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
"""

n = int(input())
res= {}
for i in range(n):
    k,v = map(int,input().split(" "))
    res.setdefault(k,0)
    res[k]=res[k]+v
for i in res.keys():
    print(i,res[i])