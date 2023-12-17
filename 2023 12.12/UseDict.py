# 使用字典--｛key:value}

# myDict = dict()
# print(myDict)
# myDict = {}
# print(myDict)
# myDict = {1: "abc", 2: "cde", 3: "wer"}
# print(myDict)
# print(myDict[2])

# 学生信息采集程序
stuDict = {}
stuList = []
# 输入--录入信息
while True:
    sno = input("请输入学号：")
    sname = input("请输入姓名：")
    cname = input("请输入班级：")
    tel = input("请输入电话：")
    flag = input("退出请按N，按其他键继续：")
    stuDict["学号"] = sno
    stuDict["姓名"] = sname
    stuDict["班级"] = cname
    stuDict["电话"] = tel
    stuList.append(stuDict)

    if flag.lower() == "n":
        break

# print(stuList)
file = open("Students.txt", "w")
file.write(str(stuList))
file.flush()
file.close()
