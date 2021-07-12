ls = [10, -11, 5, 8, 98, 66, 32]
for i in range(len(ls)):
    for j in range(len(ls) - 1):
        if ls[j] > ls[j + 1]:
            temp = ls[j + 1]
            ls[j + 1] = ls[j]
            ls[j] = temp
print(ls)
