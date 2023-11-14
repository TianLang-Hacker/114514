#判断是否是偶数


#输入
num=input("输入一个整数：")

#检查输入的内容是否整数
flag="是数字"
for ch in num:
    if ch in "1234567890":
        pass
    else:
        flag="不是数字"
    print(ch+flag)

#处理
result=""
if flag=="是数字":
    num=int(num)
    if num%2==0:
        result="是偶数"
    else:
        result="不是偶数"
else:
    result="输入的内容不是数字"

# #处理
# result=""
# if num%2==0:
#     result="是偶数"
# else:
#     result="不是偶数"

# #输出
# print(result)