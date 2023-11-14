#判断是否是偶数


#输入
num=input("输入一个整数：")

#检查输入的内容是否整数
flag=num.isdigit()



#处理
result=""
if flag==True:
    num=int(num)
    if num%2==0:
        result="是偶数"
    else:
        result="不是偶数"
else:
    result="输入的内容不是数字"

print(result)