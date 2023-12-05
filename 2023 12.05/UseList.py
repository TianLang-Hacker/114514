# """""
# 输入三个数，从大到小排列输出
# """""
# # 1、输入三个数，从大到小排列输出
# numList = []  # 定义了一个空的列表
# # 输出
# num1 = input("输入第一个数：")
# numList.append(num1)
# num2 = input("输入第二个数：")
# numList.append(num2)
# num3 = input("输入第三个数：")
# numList.append(num3)
#
# # 处理
# numList.sort(reverse=True)
#
# print(numList)

# 2、输入任意数的整数，按照输入的顺序一个个输出
numList = []

st = input()
numList = st.split(",")

num = len(numList)
for i in range(num):
    print(numList.pop())
