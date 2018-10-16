sum = 0
i = 2
for i in range(2, 10):
    j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        sum += i
print(sum)
