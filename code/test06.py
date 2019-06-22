
"""
编写一个函数，计算字符串中含有的不同字符的个数。
字符在ACSII码范围内(0~127)。不在范围内的不作统计。
"""

strings = input()
print(len(set(strings)))