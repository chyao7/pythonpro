
"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
"""

num = input()[::-1]

k = []

for i in num:
    if i not in k:
        k.append(i)
print("".join(k))