# 读取文件中的数据
# file=open("114514.txt","r")
# st=file.read()
# print(st)

# 输出有几个人
# file=open("114514.txt","r")
# st=file.read()
# result=st.count(",")
# print(result)

# 将文件中的名单以下列格式输出，每行一个“学号，姓名”
# file=open("114514.txt","r")
# st=file.read()
# result=st.replace(";","\n")
# print(result)

# 仅仅保留文件中的学号

# file=open("114514.txt","r")
# st=file.read()
#
# result=""
# num=st.count(",")
# for i in range(num):
#     dIndex=st.find(",")
#     fIndex=st.find(";")
#     sno=st[0:dIndex]
#     st=st[fIndex+1:]
#     result+=sno+"\n"
#
#     print(result)

# 取出姓张的同学的学号和姓名
# file = open("114514.txt", "r")
# st = file.read()
#
# result = ""
# num = st.count(",")  # 取学生数量
# for i in range(num):
#     dIndex = st.find(",")
#     fIndex = st.find(";")
#     sno = st[0:dIndex]  # 取学号
#     sname = st[dIndex + 1:fIndex]  # 取姓名
#     st = st[fIndex + 1:]  # 去掉第一个学生的信息
#     if sname.startswith("李"):
#         result += sno + ',' + sname + ";"
#
# print(result)

# 输出学号和姓名时，将学号5~8位用*代替，姓名仅仅保留姓，其余用*代替
# 例：2022****2，李**
file = open("114514.txt", "r")
st = file.read()

result = ""
num = st.count(",")  # 取学生数量
for i in range(num):
    dIndex = st.find(",")
    fIndex = st.find(";")
    sno = st[0:dIndex]  # 取学号
    sname = st[dIndex + 1:fIndex]  # 取姓名
    sno=sno[0:4]+"****"+sno[-1]
    sname=sname[0] + "**"
    result+=sno+","+sname+"\n"

print(result)
