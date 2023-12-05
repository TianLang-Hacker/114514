# # 读文件
# file = open("1.txt", "r")
# students = file.read()
#
# result = students.replace(";", "\n")
#
# # 写文件
# filel = open("new.txt", "w")
# filel.write(result)
# filel.flush()
# filel.close()

# 只保留学号
# file = open("new.txt", "r")
#
# result = ""
# for student in file:
#     result += student[0:10]
#
# print(result)

# file = open("new.txt", "r")
# students = file.read()
#
# result = students.split("\n")
#
# # print(result[0]) #第0位学生
# # print(result[1]) #第1位学生
# # print(result[2])  # 第2位学生

# # 将1.txt中的内容转换成列表，输出第十个学生的信息
# file = open("1.txt", "r")
# students = file.read()
#
# result = ""
# myList = students.split(";")
#
# print(myList[9])

# # 倒序输出所有学生的信息
# file = open("1.txt", "r")
# students = file.read()
#
# result = students[::-1]
#
# print(result)
