# flag = 10
# while flag:
#     print(flag)
#     flag -= 1
# flag = -10
# while flag:
#     print(flag)
#     flag += 1
# 老男孩练习题
# 使用while循环输入 1 2 3 4 5 6     8 9 10
# while True:
#     print(input(">>>"))
# 求1-100的所有数的和
# 方法1
# a = 0
# for i in range(1, 101):
#     a += i
#     print(a)
# # 方法2
# a = 0
# count = 0
# while count <= 100:
#     a += count
#     count += 1
#     print(a)

# 输出 1-100 内的所有奇数
# for i in range(1, 100, 2):
#     print(i)

# a = 1
# while a < 100:
#     if a == 99:
#         break
#     a += 2
#     print(a)
# # 输出 1-100 内的所有偶数
# 方法1
# for i in range(2, 100, 2):
#     print(i)
# 方法2
# a = 0
# while a < 100:
#     if a == 100:
#         break
#     a += 2
#     print(a)
# 求1-2+3-4+5 ... 99的所有数的和

# 用户登陆（三次机会重试）
# 方法1
# username = 'admin'
# password = 'admin'
#
# for i in range(1, 4):
#     user = input("username:")
#     passwd = input("password:")
#     if user == username and passwd == password:
#         print("wlecome to login")
#         break
#     else:
#         print("wrong! wrong")
#         continue

# 方法2
# username = 'admin'
# password = 'admin'
#
# a = 3
# while a >= 1:
#     user = input("username:")
#     passwd = input("password:")
#     if user == username and passwd == password:
#         print("welcome to login")
#         break
#     else:
#         print("wrong! wrong")
# 作业：⽤用户登录
# 1. 三次重试机会
# 2. 每次输错误时显⽰示剩余错误次数
# 方法1
username = 'admin'
password = 'admin'
a = 3
for i in range(2, -1, -1):
    user = input("username:")
    passwd = input("password:")
    if user == username and passwd == password:
        print("welcome to login")
        break
    else:
        print("wrong! wrong")
        print(i)
        continue


# 方法2
a = 3
while a >= 1:
    user = input("username:")
    passwd = input("password:")
    if user == username and passwd == password:
        print("welcome to login")
        break
    else:
        print("wrong! wrong")
        a -= 1
        print(a)

age = int(input("age:"))
if age < 50:
    if 10 < age < 20:
        pass
    elif 20 < age < 30:
        pass
    elif 30 < age < 40:
        pass
    elif 40 < age < 50:
        pass
    else:
        print("小屁孩")
elif age > 50:
    if age < 60:
        pass
    elif 60 < age < 70:
        pass
    elif 70 < age < 90:
        pass
    else:
        pass

