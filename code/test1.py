
weight = list((map(int,input().split(','))))
weight2 = list((map(int,input().split(','))))
value = [weight2[i]-weight[i] for i in range(len(weight))]
weight_most = int(input())

def bag_0_1(weight, value, weight_most):
    num = len(weight)
    weight.insert(0, 0)
    value.insert(0, 0)
    bag = [[0 for i in range(weight_most+ 1)] for j in range(num + 1)]
    for i in range(1, num + 1):
        for j in range(1, weight_most + 1):
            if weight[i] <= j:
                bag[i][j] = max(bag[i - 1][j - weight[i]] + value[i], bag[i - 1][j])
            else:
                bag[i][j] = bag[i - 1][j]
    # print(bag)
    return bag[-1][-1]


result = bag_0_1(weight, value, weight_most)
print(result+sum(weight))

