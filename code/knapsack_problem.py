
def compKnapOpt(num,capacity,weightList,valueList):
    """
    0-1背包问题
    """
    valueExcel = [[0 for i in range(capacity + 1)] for j in range(num+1)]
    for i in range(1, num + 1):
        for j in range(1, capacity + 1):
            valueExcel[i][j] = valueExcel[i-1][j]
            if weightList[i-1]<=j and valueExcel[i][j]<valueExcel[i][j-weightList[i-1]]+valueList[i-1]:
                valueExcel[i][j] = valueExcel[i-1][j - weightList[i - 1]] + valueList[i - 1]
                if j == capacity:
                    print(i)
    return valueExcel


def compKnapOpt02(num,capacity,weightList,valueList):
    """
    完全背包问题
    """
    valueExcel = [0 for j in range(capacity + 1)]
    for i in range(1, num + 1):
        for j in range(1, capacity + 1):
            if weightList[i-1]<=j:
                valueExcel[j] = max(valueExcel[j - weightList[i - 1]] + valueList[i - 1], valueExcel[j])
    return valueExcel
# print(compKnapOpt02(5,16,[5,4,7,2,6],[12,3,10,3,6]))
print(compKnapOpt(5,10,[2,2,6,5,4],[3,6,5,4,6]))