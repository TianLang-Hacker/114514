#输出1114~1314之间的所有字符，用逗号分隔开
# for i in range(1114,1314):
#     print (chr(i),end=',')
#
# for i in range(200):
#     code=1114+i
#     print(chr(code),end=",")

#输出编码在1114~1214之间的字符和编码，格式为“字符：编码”

# for i in range(1114,1214):
#     print(chr(i),end=",")
#     print(":",end="")
#     print(i)

# i=1114
# while i<1214:
#     print(chr(i),":",i)
#     i=i+1

# # 输出以下字符的编码：“TianLang-Hacker”
# for ch in "TianLang-Hacker":
#     print(ord(ch))

#输出所有大小写字符的编码
# i=97
# while i<122:
#     print(chr(i),end="")
#     i=i+1

# i=65
# while i<90:
#     print(chr(i),end="")
#     i=i+1

#输出所有大小写字母的编码，格式为“编码：字符”
for i in range(97,123):
    print(chr(i),end=",")
    print(":",end="")
    print(i)

for i in range(65,91):
    print(chr(i),end=",")
    print(":",end="")
    print(i)