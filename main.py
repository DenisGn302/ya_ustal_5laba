x = [25, 12, 99, 51, 87, 63, 44, 104, 992, 523]
for i in range(1, len(x), 2):
    x[i] = x[i] + x[i - 1]
print(x)