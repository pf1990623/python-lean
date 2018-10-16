# for i in range(10, 0, -1):
#     print(i)
# for i in range(10):
#     if i % 2:
#         continue
#     print(i)
#
# for i in range(10):
#     if not i % 2:
#         print(i)
#
# for i in range(10):
#     if not i & 0x01:
#         print(i)
#
# for i in range(10):
#     if i & 0x01:
#         continue
#     print(i)

# count = 0
# for i in range(0,1000,7):
#     print(i)
#     count += 1
#     if count >= 20:
#         break

# 练习题
# 打印一个边长为N的正方向
# n = int(input(">>>"))
# print(n*'*')
# for i in range(n-2):
#     print("*", ''*(i-1), '*')
# print(n*'*')
# for i in range(4)
# 求100内所有奇数的和（2500）
# n = 0
# for i in range(1, 100, 2):
#     n += i
# print(n)
# 判断学生成绩，成绩等级A-E。其中90分以上为A，８０－８９分为B，７０－７９为C　６０－６９为D，６０为E
# store = int(input("store"))
# if store > 90:
#     print("A")
# elif 80 <= store <=89:
#     print("B")
# elif 70 <= store <=79:
#     print("C")
# elif 60 <= store <=69:
#     print("D")
# else:
#     print("E")


# 求1-5阶乘之和
# n = 1
# for i in range(1, 6):
#     n *= i
# print(n)
# n = 5
# a = 1
# while n > 1:
#     a *= n
#     n -= 1
# print(a)

# n = 1
# a = 1
# while n < 6:
#     a *= n
#     n += 1
# print(a)
# 给一个数，判断是否是素数（质数）
#   质数：大于1的自然数只能被1和他本身整除
# n = int(input(">>>"))
# for i in range(2, n):
#     if n % i == 0:
#         print("不是质数")
#         break
# else:
#     print("是质数")


# 打印99 乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j > i:
#             print("")
#             break
#         print(j, "*", i, "=", i*j, end='\t')

# 打印菱形
# 打印100以内裴波纳契数列
# x = 0
# y = 1
# while True:
#     z = x + y
#     x = y
#     y = z
#     if z > 100:
#         break
#     print(z)


# 求裴波纳契数列第101项
# x = 0
# y = 1
# count = 0
# while True:
#     z = x + y
#     x = y
#     y = z
#     count += 1
#     if count > 102:
#         print(z)
#         break

# 求10W内所有的素数
sum = 0
# i = 2
for i in range(2, 100000):
    # j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        sum += i
print(sum)
# n = int(input(">>>"))
# print(2 // 5 > 0)
# sum = 0
# i = 2
# for i in range(2, 10):
#     # j = 2
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         sum += i
# print(sum)
# sum = 0
# i = 2
# for i in range(2, 10):
#     # j = 2
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         sum += i
# print(sum)