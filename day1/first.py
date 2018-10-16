# print("abc")
# print(~12)
# print(10^9)
# print(10^-9)

# 输入两个数字，输出最大数
a = int(input(">>>"))
b = int(input(">>>"))
if a > b:
    print(a)
else:
    print(b)

# 给定一个不超过5位的正整数，判读其有几位
c = int(input(">>>"))
if c > 100000:
    print("5 位数")
elif c > 10000:
    print(5)
elif c > 1000:
    print(4)
elif c > 100:
    print(3)
elif c > 10:
    print(2)
else:
    print(1)
